from datetime import datetime
from ..utils.indicators import INDICATORS_CONFIG, PINYIN_TO_INDICATOR, get_risk_level, calculate_overall_risk, get_sensitivity_coefficient
from .pdf_generator import PDFReportGenerator

class RiskEvaluator:
    def __init__(self):
        self.pdf_generator = PDFReportGenerator()
    
    def _convert_zbxx_format(self, zbxx):
        """将拼音编码输入转换为indicator_xxx格式，并将字符串值转换为整数"""
        converted_zbxx = {}
        
        for key, value in zbxx.items():
            # 将字符串值转换为整数
            try:
                int_value = int(value)
            except (ValueError, TypeError):
                print(f"警告：指标 {key} 的值 '{value}' 无法转换为整数，跳过此指标")
                continue
            
            # 检查是否是拼音编码格式
            if key in PINYIN_TO_INDICATOR:
                # 转换拼音编码为indicator_xxx格式
                indicator_id = PINYIN_TO_INDICATOR[key]
                converted_zbxx[indicator_id] = int_value
            elif key.startswith('indicator_'):
                # 已经是indicator_xxx格式，直接使用
                converted_zbxx[key] = int_value
            else:
                # 未知格式，跳过或记录警告
                print(f"警告：未识别的指标编码 {key}")
        
        return converted_zbxx
    
    def evaluate(self, indicator_data):
        """评估风险并生成报告"""
        jcxx = indicator_data.jcxx
        zbxx = indicator_data.zbxx
        mgdxx = indicator_data.mgdxx  # 敏感度信息
        
        # 转换输入格式（支持拼音编码和indicator_xxx两种格式）
        converted_zbxx = self._convert_zbxx_format(zbxx)
        
        # 计算敏感度系数
        sensitivity_coefficient = 1.0
        if mgdxx:
            sensitivity_coefficient = get_sensitivity_coefficient(
                mgdxx.sensitive_time,
                mgdxx.sensitive_area, 
                mgdxx.sensitive_attribute
            )
        
        # 存储每个指标的详细风险信息
        detail_risks = {}
        
        for indicator_id, indicator_value in converted_zbxx.items():
            if indicator_id in INDICATORS_CONFIG:
                config = INDICATORS_CONFIG[indicator_id]
                
                # 获取风险矩阵
                risk_matrix = config["risk_matrix"].get(indicator_value, {})
                
                if risk_matrix:
                    possibility = risk_matrix["possibility"]
                    severity = risk_matrix["severity"]
                    risk_value = possibility * severity
                    risk_level = get_risk_level(risk_value)
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
                        indicator_value             # 指标值
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
            "calculation_method": f"综合风险计算公式: α = k(1+l/50)∑(wi*ri)"  # 计算方法说明
        }
        
        # 生成PDF报告
        try:
            pdf_path = self.pdf_generator.generate_risk_report(response_data)
            response_data["filePath"] = pdf_path
        except Exception as e:
            print(f"PDF生成失败: {e}")
            response_data["filePath"] = "PDF生成失败"
        
        return response_data 