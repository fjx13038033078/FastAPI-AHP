#!/usr/bin/env python3
"""
风险评估接口测试脚本
"""
import json
import requests
import time
import os

# API配置
API_BASE_URL = "http://localhost:8000"
RISK_EVALUATE_URL = f"{API_BASE_URL}/api/risk/evaluate"
HEALTH_URL = f"{API_BASE_URL}/api/health"

def load_test_data():
    """加载测试数据"""
    # 获取当前脚本所在目录的test_data.json
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(current_dir, 'test_data.json')
    
    with open(test_data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def test_health():
    """测试健康检查接口"""
    print("🔍 测试健康检查接口...")
    try:
        response = requests.get(HEALTH_URL)
        print(f"✅ 健康检查: {response.status_code} - {response.json()}")
        return True
    except Exception as e:
        print(f"❌ 健康检查失败: {e}")
        return False

def test_risk_evaluate(test_name, test_data, description):
    """测试风险评估接口"""
    print(f"\n🧪 测试案例: {test_name}")
    print(f"📝 描述: {description}")
    
    try:
        response = requests.post(RISK_EVALUATE_URL, json=test_data)
        
        if response.status_code == 200:
            result = response.json()
            data = result.get('data', {})
            print(f"✅ 状态: {response.status_code}")
            print(f"🎯 风险等级: {data.get('level', 'Unknown')}")
            print(f"📊 敏感度系数: {data.get('sensitivity_coefficient', 'N/A')}")
            print(f"📈 调整后风险值: {data.get('adjusted_risk_value', 'N/A')}")
            print(f"📄 生成报告: {data.get('filePath', 'N/A')}")
            print(f"🔢 有效指标数量: {data.get('indicator_count', 'N/A')}")
        else:
            print(f"❌ 失败: {response.status_code}")
            print(f"🚨 错误信息: {response.text}")
            
    except Exception as e:
        print(f"❌ 请求异常: {e}")

def main():
    """主函数"""
    print("🚀 开始测试风险评估接口...")
    print("=" * 60)
    
    # 健康检查
    if not test_health():
        print("❌ 服务未启动，请先启动FastAPI服务")
        return
    
    # 加载测试数据
    try:
        test_data = load_test_data()
    except FileNotFoundError:
        print("❌ 找不到test_data.json文件")
        return
    except json.JSONDecodeError:
        print("❌ test_data.json格式错误")
        return
    
    print("\n" + "=" * 60)
    print("📋 开始执行测试用例")
    
    # 测试快速用例
    quick_test = test_data.get('quick_test')
    if quick_test:
        test_risk_evaluate(
            "quick_test", 
            quick_test,
            quick_test.get('description', '快速测试')
        )
    
    # 测试所有测试案例
    test_cases = test_data.get('test_cases', {})
    for case_name, case_data in test_cases.items():
        test_risk_evaluate(
            case_name,
            case_data.get('data', {}),
            case_data.get('description', '无描述')
        )
        time.sleep(0.5)  # 避免请求过于频繁
    
    print("\n" + "=" * 60)
    print("✅ 所有测试完成!")

if __name__ == "__main__":
    main() 