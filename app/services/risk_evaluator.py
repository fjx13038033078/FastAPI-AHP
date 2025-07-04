from datetime import datetime
from ..utils.indicators import INDICATORS_CONFIG, PINYIN_TO_INDICATOR, get_risk_level, calculate_overall_risk, get_sensitivity_coefficient, calculate_multi_select_risk
from .pdf_generator import PDFReportGenerator

class RiskEvaluator:
    def __init__(self):
        self.pdf_generator = PDFReportGenerator()
    
    def _convert_zbxx_format(self, zbxx):
        """将拼音编码输入转换为indicator_xxx格式，并将字符串值转换为整数"""
        converted_zbxx = {}
        
        for key, value in zbxx.items():
            # 处理多选指标的情况（数组格式）
            if isinstance(value, list):
                # 如果是数组，将每个元素转换为整数
                try:
                    int_values = [int(v) for v in value]
                except (ValueError, TypeError):
                    print(f"警告：指标 {key} 的数组值 '{value}' 包含无法转换为整数的元素，跳过此指标")
                    continue
            else:
                # 单个值的情况
                try:
                    int_values = int(value)
                except (ValueError, TypeError):
                    print(f"警告：指标 {key} 的值 '{value}' 无法转换为整数，跳过此指标")
                    continue
            
            # 检查是否是拼音编码格式
            if key in PINYIN_TO_INDICATOR:
                # 转换拼音编码为indicator_xxx格式
                indicator_id = PINYIN_TO_INDICATOR[key]
                converted_zbxx[indicator_id] = int_values
            elif key.startswith('indicator_'):
                # 已经是indicator_xxx格式，直接使用
                converted_zbxx[key] = int_values
            else:
                # 未知格式，跳过或记录警告
                print(f"警告：未识别的指标编码 {key}")
        
        return converted_zbxx
    
    def _convert_mgdxx_format(self, mgdxx):
        """将敏感度信息的字符串值转换为整数"""
        if not mgdxx:
            return None
        
        try:
            # 如果mgdxx是字典类型，直接处理
            if isinstance(mgdxx, dict):
                converted_mgdxx = {}
                for key, value in mgdxx.items():
                    try:
                        converted_mgdxx[key] = int(str(value).strip())
                    except (ValueError, TypeError):
                        print(f"警告：敏感度指标 {key} 的值 '{value}' 无法转换为整数，使用默认值0")
                        converted_mgdxx[key] = 0
                return converted_mgdxx
            else:
                # 如果mgdxx是对象类型，转换其属性
                converted_mgdxx = {}
                for attr in ['sensitive_time', 'sensitive_area', 'sensitive_attribute']:
                    if hasattr(mgdxx, attr):
                        value = getattr(mgdxx, attr)
                        try:
                            converted_mgdxx[attr] = int(str(value).strip())
                        except (ValueError, TypeError):
                            print(f"警告：敏感度指标 {attr} 的值 '{value}' 无法转换为整数，使用默认值0")
                            converted_mgdxx[attr] = 0
                    else:
                        converted_mgdxx[attr] = 0
                return converted_mgdxx
        except Exception as e:
            print(f"警告：处理敏感度信息时出错: {e}")
            return {
                'sensitive_time': 0,
                'sensitive_area': 0,
                'sensitive_attribute': 0
            }
    
    def evaluate(self, indicator_data):
        """评估风险并生成报告"""
        jcxx = indicator_data.jcxx
        zbxx = indicator_data.zbxx
        mgdxx = indicator_data.mgdxx  # 敏感度信息
        
        # 转换输入格式（支持拼音编码和indicator_xxx两种格式）
        converted_zbxx = self._convert_zbxx_format(zbxx)
        
        # 转换敏感度信息格式（支持字符串值）
        converted_mgdxx = self._convert_mgdxx_format(mgdxx)
        
        # 计算敏感度系数
        sensitivity_coefficient = 1.0
        if converted_mgdxx:
            sensitivity_coefficient = get_sensitivity_coefficient(
                converted_mgdxx.get('sensitive_time', 0),
                converted_mgdxx.get('sensitive_area', 0), 
                converted_mgdxx.get('sensitive_attribute', 0)
            )
        
        # 存储每个指标的详细风险信息
        detail_risks = {}
        
        for indicator_id, indicator_value in converted_zbxx.items():
            if indicator_id in INDICATORS_CONFIG:
                config = INDICATORS_CONFIG[indicator_id]
                
                # 使用新的多选指标处理函数
                possibility, severity, risk_value, risk_level, selected_value = calculate_multi_select_risk(
                    indicator_id, indicator_value, config
                )
                
                suggestion = config["suggestion"]
                
                # 构建详细信息数组
                detail_info = [
                    str(possibility),           # 指标可能性等级
                    str(severity),              # 指标危害程度等级
                    str(risk_value),            # 指标风险值
                    risk_level,                 # 指标风险等级
                    suggestion,                 # 对策建议
                    f"{config['level_1']}-{config['level_2']}-{config['level_3']}", # 一级-二级-三级指标
                    config["description"],      # 指标说明
                    config["index_number"],     # 指标序号
                    selected_value             # 最终选择的指标值（多选时为最高风险的值）
                ]
                
                detail_risks[config["level_3"]] = detail_info
        
        # 使用新的综合风险计算公式
        overall_risk_level, adjusted_risk_value = calculate_overall_risk(detail_risks, sensitivity_coefficient)
        
        # 生成报告时间
        report_time = datetime.now().strftime("%Y-%m-%d")
        
        # 构建响应数据
        response_data = {
            "level": overall_risk_level,
            "detail": detail_risks,
            "report_time": report_time,
            "rwmc": jcxx.rwmc,
            "dwmc": jcxx.pgdwmc,
            "filePath": "",
            "sensitivity_coefficient": sensitivity_coefficient,  # 敏感度系数
            "adjusted_risk_value": adjusted_risk_value,         # 调整后的风险值
            "indicator_count": len(detail_risks),               # 指标数量
            "calculation_info": {
                "method": "完整风险评估逻辑",
                "formula": "根据风险等级分布确定计算方法",
                "risk_values": [int(risk_info[2]) for risk_info in detail_risks.values()],
                "max_risk_value": max([int(risk_info[2]) for risk_info in detail_risks.values()]) if detail_risks else 0,
                "calculation_case": _determine_calculation_case(detail_risks)
            }
        }
        
        # 生成PDF报告
        try:
            pdf_path = self.pdf_generator.generate_risk_report(response_data)
            response_data["filePath"] = pdf_path
        except Exception as e:
            print(f"PDF生成失败: {e}")
            response_data["filePath"] = "PDF生成失败"
        
        return response_data

def _determine_calculation_case(detail_risks):
    """确定使用的计算情况"""
    if not detail_risks:
        return "无指标数据"
    
    risk_values = [int(risk_info[2]) for risk_info in detail_risks.values()]
    max_risk = max(risk_values)
    max_risk_count = risk_values.count(max_risk)
    
    if max_risk >= 70:
        return "情况1: 存在特大风险，直接定为特大风险"
    elif all(risk_value < 21 for risk_value in risk_values):
        return "情况2: 全部为一般风险，使用综合评价计算"
    elif max_risk_count == 1 and 21 <= max_risk < 70:
        return f"情况3: 单一最大值({max_risk})，采用该风险等级"
    elif max_risk_count > 1 and 21 <= max_risk < 70:
        if 21 <= max_risk < 42:
            return f"情况4a: 多个较大风险最大值({max_risk})，重新加权计算"
        else:
            return f"情况4b: 多个重大风险最大值({max_risk})，重新加权计算"
    else:
        return "未知情况" 