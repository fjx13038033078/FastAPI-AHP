#!/usr/bin/env python3
"""
多选指标测试脚本
"""
import json
import requests
import os

# API配置
API_BASE_URL = "http://localhost:8000"
RISK_EVALUATE_URL = f"{API_BASE_URL}/api/risk/evaluate"

def test_multi_select_indicators():
    """测试多选指标功能"""
    
    # 测试数据：包含多选指标
    test_data = {
        "jcxx": {
            "rwmc": "多选指标测试任务",
            "pgdwmc": "测试单位"
        },
        "zbxx": {
            # 弹药类型多选：包含轻武器弹药(0)和航空弹药(2)，应该选择航空弹药的高风险
            "dylx": ["0", "2"],  # 0=轻武器弹药(3*4=12), 2=航空弹药(7*8=56) -> 选择56
            
            # 道路类型多选：包含高速(0)和三级公路(3)，应该选择三级公路的高风险  
            "dllx": ["0", "3"],  # 0=高速(2*3=6), 3=三级公路(7*6=42) -> 选择42
            
            # 车辆安全配套设备多选：包含灭火器(0)和防静电装备(2)，应该选择防静电装备的高风险
            "claqptsb": ["0", "2"],  # 0=灭火器(5*6=30), 2=防静电装备(7*8=56) -> 选择56
            
            # 普通单选指标
            "gcdyzb": "3"  # 共产党员占比
        },
        "mgdxx": {
            "sensitive_time": "1",
            "sensitive_area": "0", 
            "sensitive_attribute": "1"
        }
    }
    
    print("🧪 测试多选指标功能")
    print("=" * 60)
    print("📝 测试数据:")
    print(f"  弹药类型: {test_data['zbxx']['dylx']} (应选择最高风险)")
    print(f"  道路类型: {test_data['zbxx']['dllx']} (应选择最高风险)")
    print(f"  车辆安全: {test_data['zbxx']['claqptsb']} (应选择最高风险)")
    print()
    
    try:
        response = requests.post(RISK_EVALUATE_URL, json=test_data)
        
        if response.status_code == 200:
            result = response.json()
            data = result.get('data', {})
            detail_risks = data.get('detail', {})
            
            print("✅ 请求成功")
            print(f"🎯 总体风险等级: {data.get('level', 'Unknown')}")
            print(f"📊 敏感度系数: {data.get('sensitivity_coefficient', 'N/A')}")
            print(f"📈 调整后风险值: {data.get('adjusted_risk_value', 'N/A')}")
            print()
            
            # 检查多选指标的处理结果
            multi_select_indicators = {
                "弹药类型": "dylx",
                "道路类型": "dllx", 
                "车辆安全配套设备": "claqptsb"
            }
            
            print("📋 多选指标处理结果:")
            for display_name, pinyin_code in multi_select_indicators.items():
                if display_name in detail_risks:
                    risk_info = detail_risks[display_name]
                    print(f"  {display_name}:")
                    print(f"    可能性: {risk_info[0]}")
                    print(f"    危害程度: {risk_info[1]}")
                    print(f"    风险值: {risk_info[2]}")
                    print(f"    风险等级: {risk_info[3]}")
                    print(f"    选择的值: {risk_info[8]}")
                    print()
            
            # 添加调试信息：显示所有检测到的指标
            print("🔍 所有检测到的指标:")
            for indicator_name, risk_info in detail_risks.items():
                print(f"  {indicator_name}: 风险值={risk_info[2]}, 等级={risk_info[3]}, 选择值={risk_info[8]}")
            print()
                
        else:
            print(f"❌ 请求失败: {response.status_code}")
            print(f"🚨 错误信息: {response.text}")
            
    except Exception as e:
        print(f"❌ 请求异常: {e}")

def test_single_select_fallback():
    """测试单选指标的兼容性"""
    
    test_data = {
        "jcxx": {
            "rwmc": "单选兼容性测试",
            "pgdwmc": "测试单位"
        },
        "zbxx": {
            # 多选指标但只提供单个值
            "dylx": "2",  # 航空弹药
            
            # 普通单选指标
            "gcdyzb": "3"
        },
        "mgdxx": {
            "sensitive_time": "0",
            "sensitive_area": "0",
            "sensitive_attribute": "0"
        }
    }
    
    print("🧪 测试单选兼容性")
    print("=" * 60)
    
    try:
        response = requests.post(RISK_EVALUATE_URL, json=test_data)
        
        if response.status_code == 200:
            result = response.json()
            data = result.get('data', {})
            print("✅ 单选兼容性测试通过")
            print(f"🎯 风险等级: {data.get('level', 'Unknown')}")
        else:
            print(f"❌ 单选兼容性测试失败: {response.status_code}")
            
    except Exception as e:
        print(f"❌ 单选兼容性测试异常: {e}")

def main():
    """主函数"""
    print("🚀 开始多选指标功能测试...")
    print()
    
    # 测试多选功能
    test_multi_select_indicators()
    print()
    
    # 测试单选兼容性
    test_single_select_fallback()
    print()
    print("✅ 所有测试完成!")

if __name__ == "__main__":
    main() 