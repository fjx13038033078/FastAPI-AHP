"""
API接口输入输出格式示例
展示风险评估接口的完整请求和响应格式
"""
import json

# ========== 输入格式示例 ==========

print("=" * 80)
print("API接口输入输出格式示例")
print("=" * 80)

# 1. 使用拼音编码格式的输入参数
input_format_pinyin = {
    "jcxx": {
        "rwmc": "弹药运输任务2024-001",
        "pgdwmc": "某军械保障部队"
    },
    "zbxx": {
        "gwzlsfqq": "1",           # 岗位种类是否齐全：是
        "zygwrznxsfcwn": "1",      # 主要岗位任职年限是否超5年：是
        "sfczyrdg": "0",           # 是否存在一人多岗：否
        "gcdyzb": "3",             # 共产党员占比：76%-100%
        "sfqbtgzzsc": "1",         # 是否全部通过政治审查：是
        "sfqbcjgaqjy": "1",        # 是否全部参加过安全教育：是
        "sfqbcjgbmpx": "1",        # 是否全部参加过保密培训：是
        "scjnkhsfqbtg": "1",       # 实操技能考核是否全部通过：是
        "llzskhsfqbtg": "1",       # 理论知识考核是否全部通过：是
        "dylx": "1",               # 弹药类型：火炮与榴弹发射器弹药
        "dyzldj": "0",             # 弹药质量等级：新品
        "dyzl": "1",               # 弹药重量：10-50吨
        "dysl": "2",               # 弹药数量：500-1000箱
        "sbsfqq": "1",             # 设备是否齐全：是
        "sbzksfhl": "1",           # 设备状况是否良好：是
        "clzk": "0",               # 车辆状况：好
        "claqptsb": "3",           # 车辆安全配套设备：全部齐全
        "clsl": "1",               # 车辆数量：6-10辆
        "dllx": "0",               # 道路类型：高速
        "ysjl": "2",               # 运输距离：300-500km
        "sfybylx": "1",            # 是否有备用路线：是
        "sfjgzdbhqyhymjqy": "0",   # 是否经过重点保护区域或人员密集区域：否
        "jj": "2",                 # 季节：秋
        "tstq": "2",               # 特殊天气：雨
        "sqmq": "0",               # 社情民情：简单
        "dq": "0",                 # 敌情：无
        "bmgzsfdsw": "1",          # 保密工作是否到位：是
        "ldzzjgsfjl": "1",         # 领导组织机构是否建立：是
        "ywaqzzjg": "1",           # 有无安全组织架构：有
        "zzzrsfmq": "1",           # 组织职责是否明确：是
        "sfkzjyxl": "1",           # 是否开展教育训练：是
        "ywaqzd": "1",             # 有无安全制度：有
        "ywaqya": "1",             # 有无安全预案：有
        "ywaqss": "1",             # 有无安全设施：有
        "sftgdyjgaqqxjsjc": "1",   # 是否通过弹药结构安全性技术检查：是
        "sfjgaqfx": "1",           # 是否经过安全分析：是
        "sfjgzjps": "1",           # 是否经过专家评审：是
        "ywfxyj": "1",             # 有无风险预警：有
        "yxtldjz": "1",            # 有协调联动机制：有
        "ywjhtc": "1",             # 有无计划统筹：有
        "sfgcls": "1",             # 是否贯彻落实：是
        "ywyjcz": "1",             # 有无应急处置：有
        "sfwtsrw": "0",            # 是否为特殊任务：否
        "sfwjjrw": "1",            # 是否为紧急任务：是
        "rwsc": "1"                # 任务时长：1-3天
    }
}

print("1. 拼音编码格式输入示例：")
print(json.dumps(input_format_pinyin, ensure_ascii=False, indent=2))

print("\n" + "-" * 80)

# 2. 使用indicator_xxx格式的输入参数
input_format_indicator = {
    "jcxx": {
        "rwmc": "弹药运输任务2024-002", 
        "pgdwmc": "某后勤保障团"
    },
    "zbxx": {
        "indicator_001": 1,        # 岗位种类是否齐全：是
        "indicator_002": 1,        # 主要岗位任职年限是否超5年：是
        "indicator_003": 0,        # 是否存在一人多岗：否
        "indicator_004": 2,        # 共产党员占比：51%-75%
        "indicator_005": 1,        # 是否全部通过政治审查：是
        "indicator_010": 2,        # 弹药类型：航空弹药
        "indicator_011": 1,        # 弹药质量等级：堪用品
        "indicator_016": 0,        # 车辆状况：好
        "indicator_019": 1,        # 道路类型：一级公路
        "indicator_023": 1         # 季节：夏
    }
}

print("2. indicator_xxx格式输入示例：")
print(json.dumps(input_format_indicator, ensure_ascii=False, indent=2))

print("\n" + "=" * 80)
print("API接口返回格式示例")
print("=" * 80)

# 返回格式示例
response_format = {
    "code": 200,
    "message": "ok",
    "data": {
        "level": "较大",
        "detail": {
            "岗位种类是否齐全": [
                "2",                    # 指标可能性等级
                "2",                    # 指标危害程度等级  
                "4",                    # 指标风险值
                "一般",                  # 指标风险等级
                "1.确定缺失哪类岗位\n2.补充缺失的岗位人员",  # 对策建议
                "人员因素-岗位-岗位种类是否齐全",  # 一级-二级-三级指标
                "管理干部、库房管理员、作业人员、警戒员、安全员、驾驶员是否齐全",  # 指标说明
                1,                      # 指标序号
                1                       # 指标值
            ],
            "主要岗位任职年限是否超5年": [
                "2",
                "2", 
                "4",
                "一般",
                "1.确定主要岗位任职年限\n2.更换主要岗位人员为5年以上",
                "人员因素-岗位-主要岗位任职年限是否超5年",
                "主要岗位任职年限是否超5年",
                2,
                1
            ],
            "是否存在一人多岗": [
                "2",
                "2",
                "4", 
                "一般",
                "1.尽量避免一人多岗",
                "人员因素-岗位-是否存在一人多岗",
                "是否存在一人多岗",
                3,
                0
            ]
            # ... 更多指标详细信息
        },
        "report_time": "2025-07-01",
        "rwmc": "弹药运输任务2024-001",
        "dwmc": "某军械保障部队", 
        "filePath": "reports/risk_report_abc123def456.pdf"
    }
}

print("返回格式示例：")
print(json.dumps(response_format, ensure_ascii=False, indent=2))

print("\n" + "=" * 80)
print("API接口地址和使用方法")
print("=" * 80)

api_info = """
API接口信息：

1. 获取所有指标信息（包含拼音编码）
   GET /api/indicators
   
2. 获取拼音编码映射表  
   GET /api/indicators/mapping
   
3. 风险评估接口（支持两种输入格式）
   POST /api/risk/evaluate
   
4. 健康检查
   GET /api/health

使用示例（curl命令）：

# 获取指标信息
curl -X GET "http://localhost:8000/api/indicators"

# 获取拼音编码映射
curl -X GET "http://localhost:8000/api/indicators/mapping"  

# 风险评估（拼音编码格式）
curl -X POST "http://localhost:8000/api/risk/evaluate" \\
     -H "Content-Type: application/json" \\
     -d '{"jcxx":{"rwmc":"测试任务","pgdwmc":"测试单位"},"zbxx":{"gwzlsfqq":"1","zygwrznxsfcwn":"1"}}'

# 风险评估（indicator格式）  
curl -X POST "http://localhost:8000/api/risk/evaluate" \\
     -H "Content-Type: application/json" \\
     -d '{"jcxx":{"rwmc":"测试任务","pgdwmc":"测试单位"},"zbxx":{"indicator_001":1,"indicator_002":1}}'

注意事项：
1. 支持拼音编码和indicator_xxx两种输入格式
2. 可以在同一请求中混合使用两种格式
3. 所有指标值都应该是整数（0,1,2,3...）
4. 系统会自动生成PDF报告并返回文件路径
5. 风险等级分为：一般、较大、重大、特大
"""

print(api_info)

print("=" * 80)
print("完整的45个指标拼音编码对照表")
print("=" * 80)

# 导入指标配置
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.utils.indicators import INDICATORS_CONFIG

print(f"{'序号':<4} {'拼音编码':<20} {'indicator_xxx':<15} {'指标名称'}")
print("-" * 80)

for indicator_id, config in INDICATORS_CONFIG.items():
    index_num = config["index_number"]
    pinyin_code = config["pinyin_code"]
    level_3 = config["level_3"]
    print(f"{index_num:<4} {pinyin_code:<20} {indicator_id:<15} {level_3}") 