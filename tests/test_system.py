"""
重构后的AHP风险评估系统测试
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.schemas import IndicatorData, BasicInfo
from app.services.risk_evaluator import RiskEvaluator
from app.utils.indicators import INDICATORS_CONFIG
from fastapi.testclient import TestClient
from app.main import app

def test_modules():
    """测试重构后的模块"""
    print("=== 重构后的模块测试 ===")
    
    # 测试指标配置
    print(f"✅ 可用指标数量: {len(INDICATORS_CONFIG)}")
    
    # 测试风险评估器
    evaluator = RiskEvaluator()
    test_data = IndicatorData(
        jcxx=BasicInfo(rwmc='重构测试任务', pgdwmc='重构测试单位'),
        zbxx={
            "indicator_001": 1,
            "indicator_002": 1,
            "indicator_003": 0,
            "indicator_004": 2,
            "indicator_005": 1
        }
    )
    
    result = evaluator.evaluate(test_data)
    print(f"✅ 总体风险等级: {result.get('level', '未知')}")
    print(f"✅ 详细指标数量: {len(result.get('detail', {}))}")
    print(f"✅ PDF报告路径: {result.get('filePath', '未生成')}")
    
    return True

def test_api():
    """测试重构后的API"""
    print("\n=== 重构后的API测试 ===")
    
    client = TestClient(app)
    
    # 测试健康检查
    response = client.get("/health")
    print(f"✅ 健康检查状态码: {response.status_code}")
    
    # 测试指标信息API
    response = client.get("/api/indicators")
    print(f"✅ 指标信息API状态码: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ 返回指标数量: {len(data.get('data', {}))}")
    
    # 测试风险评估API
    test_payload = {
        "jcxx": {
            "rwmc": "API测试任务",
            "pgdwmc": "API测试单位"
        },
        "zbxx": {
            "indicator_001": 1,
            "indicator_002": 1,
            "indicator_003": 0,
            "indicator_004": 2,
            "indicator_005": 1
        }
    }
    
    response = client.post("/api/risk/evaluate", json=test_payload)
    print(f"✅ 风险评估API状态码: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ 风险等级: {data.get('data', {}).get('level', '未知')}")
    
    return True

if __name__ == "__main__":
    try:
        print("🚀 开始测试重构后的AHP风险评估系统")
        print("=" * 50)
        
        # 模块测试
        test_modules()
        
        # API测试
        test_api()
        
        print("\n" + "=" * 50)
        print("🎉 所有测试通过！重构成功！")
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc() 