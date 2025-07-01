"""
实际API测试脚本
演示真实的API调用和响应
"""
import requests
import json
import time

# API基础URL
BASE_URL = "http://localhost:8000"

def test_api_endpoints():
    """测试所有API端点"""
    print("=" * 80)
    print("实际API测试")
    print("=" * 80)
    
    # 等待服务器启动
    print("等待服务器启动...")
    time.sleep(3)
    
    try:
        # 1. 健康检查
        print("1. 测试健康检查接口")
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"状态码: {response.status_code}")
        print(f"响应: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        print("-" * 60)
        
        # 2. 获取指标信息
        print("2. 测试获取指标信息接口")
        response = requests.get(f"{BASE_URL}/api/indicators")
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"返回指标数量: {len(data['data'])}")
        print("前3个指标信息:")
        for i, (key, value) in enumerate(list(data['data'].items())[:3]):
            print(f"  {key}: {value['level_3']} (拼音: {value['pinyin_code']})")
        print("-" * 60)
        
        # 3. 获取拼音编码映射
        print("3. 测试获取拼音编码映射接口")
        response = requests.get(f"{BASE_URL}/api/indicators/mapping")
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"映射数量: {data['data']['mapping_count']}")
        print("前5个映射:")
        for i, (pinyin, indicator) in enumerate(list(data['data']['pinyin_to_indicator'].items())[:5]):
            print(f"  {pinyin} -> {indicator}")
        print("-" * 60)
        
        # 4. 测试拼音编码格式的风险评估
        print("4. 测试拼音编码格式的风险评估")
        test_data_pinyin = {
            "jcxx": {
                "rwmc": "API测试任务-拼音格式",
                "pgdwmc": "测试单位"
            },
            "zbxx": {
                "gwzlsfqq": 0,              # 岗位种类是否齐全：否（高风险）
                "zygwrznxsfcwn": 0,         # 主要岗位任职年限是否超5年：否（高风险）
                "sfczyrdg": 1,              # 是否存在一人多岗：是（中风险）
                "gcdyzb": 0,                # 共产党员占比：0%-25%（中高风险）
                "dylx": 3,                  # 弹药类型：特种弹药（最高风险）
                "clzk": 1,                  # 车辆状况：一般（中风险）
                "jj": 1                     # 季节：夏（中风险）
            }
        }
        
        response = requests.post(
            f"{BASE_URL}/api/risk/evaluate",
            json=test_data_pinyin,
            headers={"Content-Type": "application/json"}
        )
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"总体风险等级: {data['data']['level']}")
        print(f"任务名称: {data['data']['rwmc']}")
        print(f"评估指标数量: {len(data['data']['detail'])}")
        print(f"PDF文件路径: {data['data']['filePath']}")
        print("详细风险信息:")
        for indicator_name, detail_info in list(data['data']['detail'].items())[:3]:
            risk_value = detail_info[2]
            risk_level = detail_info[3]
            print(f"  {indicator_name}: 风险值={risk_value}, 风险等级={risk_level}")
        print("-" * 60)
        
        # 5. 测试indicator_xxx格式的风险评估
        print("5. 测试indicator_xxx格式的风险评估")
        test_data_indicator = {
            "jcxx": {
                "rwmc": "API测试任务-indicator格式",
                "pgdwmc": "测试单位"
            },
            "zbxx": {
                "indicator_001": 1,         # 岗位种类是否齐全：是
                "indicator_002": 1,         # 主要岗位任职年限是否超5年：是
                "indicator_003": 0,         # 是否存在一人多岗：否
                "indicator_004": 3,         # 共产党员占比：76%-100%
                "indicator_010": 0          # 弹药类型：轻武器弹药
            }
        }
        
        response = requests.post(
            f"{BASE_URL}/api/risk/evaluate",
            json=test_data_indicator,
            headers={"Content-Type": "application/json"}
        )
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"总体风险等级: {data['data']['level']}")
        print(f"任务名称: {data['data']['rwmc']}")
        print(f"评估指标数量: {len(data['data']['detail'])}")
        print(f"PDF文件路径: {data['data']['filePath']}")
        print("-" * 60)
        
        # 6. 测试混合格式的风险评估
        print("6. 测试混合格式的风险评估")
        test_data_mixed = {
            "jcxx": {
                "rwmc": "API测试任务-混合格式",
                "pgdwmc": "测试单位"
            },
            "zbxx": {
                "gwzlsfqq": 0,              # 拼音编码格式
                "indicator_002": 1,         # indicator_xxx格式
                "sfczyrdg": 0,              # 拼音编码格式
                "indicator_004": 2,         # indicator_xxx格式
                "dylx": 1                   # 拼音编码格式
            }
        }
        
        response = requests.post(
            f"{BASE_URL}/api/risk/evaluate",
            json=test_data_mixed,
            headers={"Content-Type": "application/json"}
        )
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"总体风险等级: {data['data']['level']}")
        print(f"任务名称: {data['data']['rwmc']}")
        print(f"评估指标数量: {len(data['data']['detail'])}")
        print(f"PDF文件路径: {data['data']['filePath']}")
        print("-" * 60)
        
        print("✓ 所有API测试完成！")
        
    except requests.exceptions.ConnectionError:
        print("❌ 无法连接到服务器，请确保服务器已启动")
        print("启动命令: python run.py")
    except Exception as e:
        print(f"❌ 测试过程中出现错误: {e}")

if __name__ == "__main__":
    test_api_endpoints() 