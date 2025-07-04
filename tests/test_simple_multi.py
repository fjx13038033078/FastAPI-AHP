#!/usr/bin/env python3
import json
import requests

# 简单的多选测试
test_data = {
    "jcxx": {
        "rwmc": "多选测试",
        "pgdwmc": "测试单位"
    },
    "zbxx": {
        "dylx": ["0", "2"],  # 弹药类型多选
        "gcdyzb": "3"
    },
    "mgdxx": {
        "sensitive_time": "0",
        "sensitive_area": "0",
        "sensitive_attribute": "0"
    }
}

response = requests.post("http://localhost:8000/api/risk/evaluate", json=test_data)
result = response.json()

print("📋 API响应状态:", response.status_code)
print("🔍 完整响应数据:")
print(json.dumps(result, indent=2, ensure_ascii=False)) 