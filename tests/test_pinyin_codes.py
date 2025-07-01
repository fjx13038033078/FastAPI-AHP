"""
测试拼音编码功能
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.indicators import INDICATORS_CONFIG, PINYIN_TO_INDICATOR
from app.services.risk_evaluator import RiskEvaluator
from app.models.schemas import IndicatorData, BasicInfo

def test_pinyin_mapping():
    """测试拼音编码映射"""
    print("=== 测试拼音编码映射 ===")
    print(f"总共配置了 {len(INDICATORS_CONFIG)} 个指标")
    print(f"拼音编码映射表包含 {len(PINYIN_TO_INDICATOR)} 个条目")
    
    # 验证映射完整性
    missing_pinyin = []
    for indicator_id, config in INDICATORS_CONFIG.items():
        pinyin_code = config.get("pinyin_code")
        if not pinyin_code:
            missing_pinyin.append(indicator_id)
        elif pinyin_code not in PINYIN_TO_INDICATOR:
            print(f"错误：拼音编码 {pinyin_code} 未在映射表中找到")
    
    if missing_pinyin:
        print(f"警告：以下指标缺少拼音编码：{missing_pinyin}")
    else:
        print("✓ 所有指标都有拼音编码")
    
    # 展示部分映射关系
    print("\n前10个拼音编码映射：")
    for i, (pinyin, indicator) in enumerate(list(PINYIN_TO_INDICATOR.items())[:10]):
        config = INDICATORS_CONFIG[indicator]
        print(f"{i+1:2d}. {pinyin:15s} -> {indicator:15s} ({config['level_3']})")
    
    print("\n" + "="*60)

def test_pinyin_evaluation():
    """测试使用拼音编码进行风险评估"""
    print("=== 测试拼音编码风险评估 ===")
    
    # 构建测试数据（使用拼音编码格式）
    jcxx = BasicInfo(rwmc="测试任务", pgdwmc="测试单位")
    
    # 使用拼音编码格式的测试数据
    zbxx_pinyin = {
        "gwzlsfqq": 0,              # 岗位种类是否齐全：否（高风险）
        "zygwrznxsfcwn": 0,         # 主要岗位任职年限是否超5年：否（高风险）
        "sfczyrdg": 1,             # 是否存在一人多岗：是（中风险）
        "gcdyzb": 0,                # 共产党员占比：0%-25%（中高风险）
        "sfqbtgzzsc": 1,            # 是否全部通过政治审查：是（低风险）
        "dylx": 3,                  # 弹药类型：特种弹药（最高风险）
        "dyzldj": 2,                # 弹药质量等级：待修品（高风险）
        "clzk": 1,                  # 车辆状况：一般（中风险）
        "jj": 1,                    # 季节：夏（中风险）
        "tstq": 0                   # 特殊天气：雷暴（高风险）
    }
    
    # 创建指标数据
    test_data = IndicatorData(jcxx=jcxx, zbxx=zbxx_pinyin)
    
    # 执行风险评估
    evaluator = RiskEvaluator()
    result = evaluator.evaluate(test_data)
    
    print(f"任务名称：{result['rwmc']}")
    print(f"单位名称：{result['dwmc']}")
    print(f"总体风险等级：{result['level']}")
    print(f"报告时间：{result['report_time']}")
    print(f"评估指标数量：{len(result['detail'])}")
    
    print("\n详细风险评估结果：")
    for i, (indicator_name, detail_info) in enumerate(result['detail'].items(), 1):
        risk_value = detail_info[2]
        risk_level = detail_info[3]
        print(f"{i:2d}. {indicator_name:20s} 风险值:{risk_value:3s} 风险等级:{risk_level}")
    
    print("\n" + "="*60)

def test_mixed_format():
    """测试混合格式输入"""
    print("=== 测试混合格式输入 ===")
    
    jcxx = BasicInfo(rwmc="混合格式测试", pgdwmc="测试单位")
    
    # 混合使用拼音编码和indicator_xxx格式
    zbxx_mixed = {
        "gwzlsfqq": 0,              # 拼音编码格式
        "indicator_002": 1,         # indicator_xxx格式
        "sfczyrdg": 0,             # 拼音编码格式
        "indicator_004": 2,         # indicator_xxx格式
        "dylx": 1,                  # 拼音编码格式
    }
    
    test_data = IndicatorData(jcxx=jcxx, zbxx=zbxx_mixed)
    
    evaluator = RiskEvaluator()
    result = evaluator.evaluate(test_data)
    
    print(f"混合格式评估结果 - 总体风险等级：{result['level']}")
    print(f"成功评估了 {len(result['detail'])} 个指标")
    
    for indicator_name, detail_info in result['detail'].items():
        risk_level = detail_info[3]
        print(f"  {indicator_name}: {risk_level}")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    # 运行所有测试
    test_pinyin_mapping()
    test_pinyin_evaluation() 
    test_mixed_format()
    
    print("✓ 所有拼音编码测试完成！") 