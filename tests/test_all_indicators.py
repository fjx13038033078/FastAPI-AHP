import pytest
from fastapi.testclient import TestClient
import json
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app
from app.utils.indicators import INDICATORS_CONFIG
from app.services.risk_evaluator import RiskEvaluator

client = TestClient(app)

def test_all_indicators_configured():
    """测试所有45个指标是否正确配置"""
    # 检查指标数量
    assert len(INDICATORS_CONFIG) == 45, f"应该有45个指标，实际有{len(INDICATORS_CONFIG)}个"
    
    # 检查指标编号连续性
    for i in range(1, 46):
        indicator_key = f"indicator_{i:03d}"
        assert indicator_key in INDICATORS_CONFIG, f"缺少指标：{indicator_key}"
        
        # 检查指标基本属性
        indicator = INDICATORS_CONFIG[indicator_key]
        assert "index_number" in indicator, f"{indicator_key}缺少index_number"
        assert "level_1" in indicator, f"{indicator_key}缺少level_1"
        assert "level_2" in indicator, f"{indicator_key}缺少level_2"
        assert "level_3" in indicator, f"{indicator_key}缺少level_3"
        assert "description" in indicator, f"{indicator_key}缺少description"
        assert "suggestion" in indicator, f"{indicator_key}缺少suggestion"
        assert "risk_matrix" in indicator, f"{indicator_key}缺少risk_matrix"
        
        # 检查序号正确性
        assert indicator["index_number"] == i, f"{indicator_key}的序号应该是{i}"
        
        # 检查风险矩阵
        risk_matrix = indicator["risk_matrix"]
        assert len(risk_matrix) > 0, f"{indicator_key}的风险矩阵不能为空"
        
        for value, risk_data in risk_matrix.items():
            assert "possibility" in risk_data, f"{indicator_key}的风险矩阵缺少possibility"
            assert "severity" in risk_data, f"{indicator_key}的风险矩阵缺少severity"
            assert 1 <= risk_data["possibility"] <= 10, f"{indicator_key}的possibility应该在1-10之间"
            assert 1 <= risk_data["severity"] <= 10, f"{indicator_key}的severity应该在1-10之间"

def test_indicators_api():
    """测试指标信息API"""
    response = client.get("/api/indicators")
    assert response.status_code == 200
    
    data = response.json()
    assert "code" in data
    assert "message" in data
    assert "data" in data
    assert data["code"] == 200
    
    indicators = data["data"]
    assert len(indicators) == 45
    
    # 检查指标结构
    for indicator_key, indicator in indicators.items():
        assert "index_number" in indicator
        assert "level_1" in indicator
        assert "level_2" in indicator
        assert "level_3" in indicator
        assert "description" in indicator
        assert "suggestion" in indicator

def test_risk_evaluation_all_indicators():
    """测试使用所有45个指标进行风险评估"""
    # 构造测试数据：所有指标都使用第一个选项（通常是风险较高的选项）
    indicator_values = {}
    for i in range(1, 46):
        indicator_key = f"indicator_{i:03d}"
        # 使用每个指标的第一个可用选项
        risk_matrix = INDICATORS_CONFIG[indicator_key]["risk_matrix"]
        first_option = min(risk_matrix.keys())
        indicator_values[indicator_key] = first_option
    
    # 按照正确的数据格式构造请求
    test_data = {
        "jcxx": {
            "rwmc": "测试任务",
            "pgdwmc": "测试单位"
        },
        "zbxx": indicator_values
    }
    
    # 发送风险评估请求
    response = client.post("/api/risk/evaluate", json=test_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "code" in data
    assert "message" in data  
    assert "data" in data
    assert data["code"] == 200
    
    result_data = data["data"]
    assert "level" in result_data or "overall_risk" in result_data

def test_risk_evaluation_minimal_risk():
    """测试最小风险配置"""
    # 构造最小风险数据：选择每个指标的最低风险选项
    indicator_values = {}
    for i in range(1, 46):
        indicator_key = f"indicator_{i:03d}"
        risk_matrix = INDICATORS_CONFIG[indicator_key]["risk_matrix"]
        
        # 找到风险值最小的选项
        min_risk_value = float('inf')
        min_risk_option = None
        
        for option, risk_data in risk_matrix.items():
            risk_value = risk_data["possibility"] * risk_data["severity"]
            if risk_value < min_risk_value:
                min_risk_value = risk_value
                min_risk_option = option
        
        indicator_values[indicator_key] = min_risk_option
    
    test_data = {
        "jcxx": {
            "rwmc": "最小风险测试任务",
            "pgdwmc": "测试单位"
        },
        "zbxx": indicator_values
    }
    
    response = client.post("/api/risk/evaluate", json=test_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["code"] == 200

def test_risk_evaluation_maximum_risk():
    """测试最大风险配置"""
    # 构造最大风险数据：选择每个指标的最高风险选项
    indicator_values = {}
    for i in range(1, 46):
        indicator_key = f"indicator_{i:03d}"
        risk_matrix = INDICATORS_CONFIG[indicator_key]["risk_matrix"]
        
        # 找到风险值最大的选项
        max_risk_value = 0
        max_risk_option = None
        
        for option, risk_data in risk_matrix.items():
            risk_value = risk_data["possibility"] * risk_data["severity"]
            if risk_value > max_risk_value:
                max_risk_value = risk_value
                max_risk_option = option
        
        indicator_values[indicator_key] = max_risk_option
    
    test_data = {
        "jcxx": {
            "rwmc": "最大风险测试任务",
            "pgdwmc": "测试单位"
        },
        "zbxx": indicator_values
    }
    
    response = client.post("/api/risk/evaluate", json=test_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["code"] == 200

def test_risk_evaluator_directly():
    """直接测试RiskEvaluator类"""
    evaluator = RiskEvaluator()
    
    # 创建模拟的IndicatorData对象
    class MockBasicInfo:
        def __init__(self, rwmc, pgdwmc):
            self.rwmc = rwmc
            self.pgdwmc = pgdwmc
    
    class MockIndicatorData:
        def __init__(self, jcxx, zbxx):
            self.jcxx = jcxx
            self.zbxx = zbxx
    
    # 测试样本数据
    basic_info = MockBasicInfo("测试任务", "测试单位")
    indicator_values = {
        "indicator_001": 0,  # 岗位种类不齐全
        "indicator_002": 0,  # 任职年限不超5年
        "indicator_004": 0,  # 党员占比0%-25%
        "indicator_026": 1,  # 有敌情
    }
    
    data = MockIndicatorData(basic_info, indicator_values)
    result = evaluator.evaluate(data)
    
    assert isinstance(result, dict)
    assert "level" in result or "overall_risk" in result

def test_indicators_categories():
    """测试指标分类统计"""
    categories = {}
    
    for indicator_key, indicator in INDICATORS_CONFIG.items():
        level_1 = indicator["level_1"]
        if level_1 not in categories:
            categories[level_1] = 0
        categories[level_1] += 1
    
    # 验证指标分类数量
    expected_categories = {
        "人员因素": 9,
        "物品因素": 9,
        "环境因素": 9,
        "管理因素": 15,
        "任务因素": 3
    }
    
    for category, expected_count in expected_categories.items():
        assert categories.get(category, 0) == expected_count, \
            f"{category}应该有{expected_count}个指标，实际有{categories.get(category, 0)}个"
    
    assert sum(categories.values()) == 45

def test_health_endpoint():
    """测试健康检查接口"""
    response = client.get("/api/health")
    assert response.status_code == 200
    
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 