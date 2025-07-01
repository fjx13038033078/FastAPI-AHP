# 指标配置信息 - 45个指标项
INDICATORS_CONFIG = {
    "indicator_001": {
        "index_number": 1,
        "level_1": "人员因素",
        "level_2": "岗位",
        "level_3": "岗位种类是否齐全",
        "pinyin_code": "gwzlsfqq",  # 岗位种类是否齐全
        "description": "管理干部、库房管理员、作业人员、警戒员、安全员、驾驶员是否齐全",
        "suggestion": "1.确定缺失哪类岗位\n2.补充缺失的岗位人员",
        "risk_matrix": {
            0: {"possibility": 8, "severity": 7},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_002": {
        "index_number": 2,
        "level_1": "人员因素",
        "level_2": "岗位",
        "level_3": "主要岗位任职年限是否超5年",
        "pinyin_code": "zygwrznxsfcwn",  # 主要岗位任职年限是否超五年
        "description": "主要岗位任职年限是否超5年",
        "suggestion": "1.确定主要岗位任职年限\n2.更换主要岗位人员为5年以上",
        "risk_matrix": {
            0: {"possibility": 9, "severity": 9},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_003": {
        "index_number": 3,
        "level_1": "人员因素",
        "level_2": "岗位",
        "level_3": "是否存在一人多岗",
        "pinyin_code": "sfczyrdg",  # 是否存在一人多岗
        "description": "是否存在一人多岗",
        "suggestion": "1.尽量避免一人多岗",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 2},  # 否
            1: {"possibility": 7, "severity": 6}   # 是
        }
    },
    "indicator_004": {
        "index_number": 4,
        "level_1": "人员因素",
        "level_2": "政治素质",
        "level_3": "共产党员占比",
        "pinyin_code": "gcdyzb",  # 共产党员占比
        "description": "党员占比（党员人数÷总人数×100%）",
        "suggestion": "1.进行先期响应，组织风险决策，确定风险控制策略\n2.提前调换入党人员",
        "risk_matrix": {
            0: {"possibility": 7, "severity": 6},  # 0%-25%
            1: {"possibility": 5, "severity": 5},  # 26%-50%
            2: {"possibility": 3, "severity": 3},  # 51%-75%
            3: {"possibility": 1, "severity": 2}   # 76%-100%
        }
    },
    "indicator_005": {
        "index_number": 5,
        "level_1": "人员因素",
        "level_2": "政治素质",
        "level_3": "是否全部通过政治审查",
        "pinyin_code": "sfqbtgzzsc",  # 是否全部通过政治审查
        "description": "人员是否全部通过政治审查",
        "suggestion": "1.进行先期响应，组织风险决策，确定风险控制策略\n2.提前调换政治考核通过人员",
        "risk_matrix": {
            0: {"possibility": 8, "severity": 8},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_006": {
        "index_number": 6,
        "level_1": "人员因素",
        "level_2": "业务素质",
        "level_3": "是否全部参加过安全教育",
        "pinyin_code": "sfqbcjgaqjy",  # 是否全部参加过安全教育
        "description": "人员是否全部参加过安全教育",
        "suggestion": "1.进行先期响应，组织风险决策，确定风险控制策略\n2.开展安全教育培训会议",
        "risk_matrix": {
            0: {"possibility": 7, "severity": 7},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_007": {
        "index_number": 7,
        "level_1": "人员因素",
        "level_2": "业务素质",
        "level_3": "是否全部参加过保密培训",
        "pinyin_code": "sfqbcjgbmpx",  # 是否全部参加过保密培训
        "description": "人员是否全部参加过保密培训",
        "suggestion": "1.进行先期响应，组织风险决策，确定风险控制策略\n2.开展保密培训会议",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 6},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_008": {
        "index_number": 8,
        "level_1": "人员因素",
        "level_2": "业务素质",
        "level_3": "实操技能考核是否全部通过",
        "pinyin_code": "scjnkhsfqbtg",  # 实操技能考核是否全部通过
        "description": "实操技能考核是否全部通过",
        "suggestion": "1.进行先期响应，组织风险决策，确定风险控制策略\n2.提前调换实操技能考核通过人员",
        "risk_matrix": {
            0: {"possibility": 8, "severity": 7},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_009": {
        "index_number": 9,
        "level_1": "人员因素",
        "level_2": "业务素质",
        "level_3": "理论知识考核是否全部通过",
        "pinyin_code": "llzskhsfqbtg",  # 理论知识考核是否全部通过
        "description": "理论知识考核是否全部通过",
        "suggestion": "1.进行先期响应，组织风险决策，确定风险控制策略\n2.提前调换理论知识考核通过人员",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 6},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_010": {
        "index_number": 10,
        "level_1": "物品因素",
        "level_2": "弹药",
        "level_3": "弹药类型",
        "pinyin_code": "dylx",  # 弹药类型
        "description": "包含的弹药类型",
        "suggestion": "1.避免高风险弹药混装",
        "risk_matrix": {
            0: {"possibility": 3, "severity": 4},  # 轻武器弹药
            1: {"possibility": 5, "severity": 6},  # 火炮与榴弹发射器弹药
            2: {"possibility": 7, "severity": 8},  # 航空弹药
            3: {"possibility": 8, "severity": 9},  # 特种弹药
            4: {"possibility": 4, "severity": 5}   # 辅助弹药
        }
    },
    "indicator_011": {
        "index_number": 11,
        "level_1": "物品因素",
        "level_2": "弹药",
        "level_3": "弹药质量等级",
        "pinyin_code": "dyzldj",  # 弹药质量等级
        "description": "弹药的质量等级",
        "suggestion": "1.待修品与报废品需要加倍小心",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 新品
            1: {"possibility": 4, "severity": 4},  # 堪用品
            2: {"possibility": 7, "severity": 8},  # 待修品
            3: {"possibility": 9, "severity": 9}   # 报废品
        }
    },
    "indicator_012": {
        "index_number": 12,
        "level_1": "物品因素",
        "level_2": "弹药",
        "level_3": "弹药重量(吨)",
        "pinyin_code": "dyzl",  # 弹药重量
        "description": "弹药的重量",
        "suggestion": "1.增加运输车辆",
        "risk_matrix": {
            0: {"possibility": 3, "severity": 3},  # 0-10吨
            1: {"possibility": 5, "severity": 5},  # 10-50吨
            2: {"possibility": 7, "severity": 7},  # 50-100吨
            3: {"possibility": 9, "severity": 8}   # 100吨以上
        }
    },
    "indicator_013": {
        "index_number": 13,
        "level_1": "物品因素",
        "level_2": "弹药",
        "level_3": "弹药数量（箱）",
        "pinyin_code": "dysl",  # 弹药数量
        "description": "弹药的数量",
        "suggestion": "1.增加运输车辆",
        "risk_matrix": {
            0: {"possibility": 3, "severity": 3},  # 0-100箱
            1: {"possibility": 5, "severity": 5},  # 100-500箱
            2: {"possibility": 7, "severity": 6},  # 500-1000箱
            3: {"possibility": 8, "severity": 7}   # 1000箱以上
        }
    },
    "indicator_014": {
        "index_number": 14,
        "level_1": "物品因素",
        "level_2": "机工具",
        "level_3": "设备是否齐全",
        "pinyin_code": "sbsfqq",  # 设备是否齐全
        "description": "设备是否齐全",
        "suggestion": "1.提前准备好相应设备",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 5},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_015": {
        "index_number": 15,
        "level_1": "物品因素",
        "level_2": "机工具",
        "level_3": "设备状况是否良好",
        "pinyin_code": "sbzksfhl",  # 设备状况是否良好
        "description": "设备状况是否良好",
        "suggestion": "1.状况不好的设备及时更换",
        "risk_matrix": {
            0: {"possibility": 7, "severity": 6},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_016": {
        "index_number": 16,
        "level_1": "物品因素",
        "level_2": "运输车辆",
        "level_3": "车辆状况",
        "pinyin_code": "clzk",  # 车辆状况
        "description": "车辆状况",
        "suggestion": "1.车况不好的车辆及时更换",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 好
            1: {"possibility": 6, "severity": 6}   # 一般
        }
    },
    "indicator_017": {
        "index_number": 17,
        "level_1": "物品因素",
        "level_2": "运输车辆",
        "level_3": "车辆安全配套设备",
        "pinyin_code": "claqptsb",  # 车辆安全配套设备
        "description": "车辆安全配套设备",
        "suggestion": "1.提前准备好车辆安全配套设备",
        "risk_matrix": {
            0: {"possibility": 5, "severity": 6},  # 灭火器
            1: {"possibility": 6, "severity": 7},  # 尾气熄火塞
            2: {"possibility": 7, "severity": 8},  # 防静电装备
            3: {"possibility": 3, "severity": 4}   # 全部齐全
        }
    },
    "indicator_018": {
        "index_number": 18,
        "level_1": "物品因素",
        "level_2": "运输车辆",
        "level_3": "车辆数量（辆）",
        "pinyin_code": "clsl",  # 车辆数量
        "description": "运输车辆数量",
        "suggestion": "1.车辆数量大于20车时尽量拆分任务",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 1-5辆
            1: {"possibility": 4, "severity": 4},  # 6-10辆
            2: {"possibility": 6, "severity": 6},  # 11-20辆
            3: {"possibility": 8, "severity": 7}   # 20辆以上
        }
    },
    "indicator_019": {
        "index_number": 19,
        "level_1": "环境因素",
        "level_2": "道路",
        "level_3": "道路类型",
        "pinyin_code": "dllx",  # 道路类型
        "description": "运输道路的类型",
        "suggestion": "1.提前规划路径，尽量走高速、一级公路",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 高速
            1: {"possibility": 3, "severity": 4},  # 一级公路
            2: {"possibility": 5, "severity": 5},  # 二级公路
            3: {"possibility": 7, "severity": 6}   # 三级公路
        }
    },
    "indicator_020": {
        "index_number": 20,
        "level_1": "环境因素",
        "level_2": "道路",
        "level_3": "运输距离（km）",
        "pinyin_code": "ysjl",  # 运输距离
        "description": "运输的距离",
        "suggestion": "1.单日运输距离大于500时需要住宿休息",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 0-100km
            1: {"possibility": 4, "severity": 4},  # 100-300km
            2: {"possibility": 6, "severity": 5},  # 300-500km
            3: {"possibility": 8, "severity": 6}   # 500km以上
        }
    },
    "indicator_021": {
        "index_number": 21,
        "level_1": "环境因素",
        "level_2": "道路",
        "level_3": "是否有备用路线",
        "pinyin_code": "sfybylx",  # 是否有备用路线
        "description": "是否有备用路线",
        "suggestion": "1.提前确定备用路线",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 5},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_022": {
        "index_number": 22,
        "level_1": "环境因素",
        "level_2": "道路",
        "level_3": "是否经过重点保护区域或人员密集区域",
        "pinyin_code": "sfjgzdbhqyhymjqy",  # 是否经过重点保护区域或人员密集区域
        "description": "是否经过重点保护区域或人员密集区域",
        "suggestion": "1.经过重点保护区域或人员密集区域时降低车速",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 否
            1: {"possibility": 7, "severity": 8}   # 是
        }
    },
    "indicator_023": {
        "index_number": 23,
        "level_1": "环境因素",
        "level_2": "天气",
        "level_3": "季节",
        "pinyin_code": "jj",  # 季节
        "description": "运输时的季节",
        "suggestion": "1.夏天需要做好降温措施",
        "risk_matrix": {
            0: {"possibility": 3, "severity": 3},  # 春
            1: {"possibility": 6, "severity": 5},  # 夏
            2: {"possibility": 4, "severity": 4},  # 秋
            3: {"possibility": 5, "severity": 5}   # 冬
        }
    },
    "indicator_024": {
        "index_number": 24,
        "level_1": "环境因素",
        "level_2": "天气",
        "level_3": "特殊天气",
        "pinyin_code": "tstq",  # 特殊天气
        "description": "运输时的特殊天气",
        "suggestion": "1.特殊天气需要驻车等待",
        "risk_matrix": {
            0: {"possibility": 8, "severity": 7},  # 雷暴
            1: {"possibility": 7, "severity": 6},  # 大风
            2: {"possibility": 6, "severity": 5},  # 雨
            3: {"possibility": 7, "severity": 6},  # 雪
            4: {"possibility": 6, "severity": 6}   # 高温
        }
    },
    "indicator_025": {
        "index_number": 25,
        "level_1": "环境因素",
        "level_2": "社会因素",
        "level_3": "社情民情",
        "pinyin_code": "sqmq",  # 社情民情
        "description": "运输车辆途径地的社情与民情",
        "suggestion": "1.进行先期响应，组织风险决策，确定风险控制策略\n2.对途径的人们进行安抚",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 简单
            1: {"possibility": 7, "severity": 6}   # 复杂
        }
    },
    "indicator_026": {
        "index_number": 26,
        "level_1": "环境因素",
        "level_2": "社会因素",
        "level_3": "敌情",
        "pinyin_code": "dq",  # 敌情
        "description": "运输车辆途径地的敌情",
        "suggestion": "1.进行先期响应，组织风险决策，确定风险控制策略\n2.如遇敌情保持警戒，更改路线",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 无
            1: {"possibility": 9, "severity": 9}   # 有
        }
    },
    "indicator_027": {
        "index_number": 27,
        "level_1": "环境因素",
        "level_2": "社会因素",
        "level_3": "保密工作是否到位",
        "pinyin_code": "bmgzsfdsw",  # 保密工作是否到位
        "description": "保密工作是否到位",
        "suggestion": "1.提前做好保密工作",
        "risk_matrix": {
            0: {"possibility": 7, "severity": 6},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_028": {
        "index_number": 28,
        "level_1": "管理因素",
        "level_2": "管理组织",
        "level_3": "领导组织机构是否建立",
        "pinyin_code": "ldzzjgsfjl",  # 领导组织机构是否建立
        "description": "领导组织机构是否建立",
        "suggestion": "1.提前建立良好的领导组织机构",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 5},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_029": {
        "index_number": 29,
        "level_1": "管理因素",
        "level_2": "管理组织",
        "level_3": "有无安全组织架构",
        "pinyin_code": "ywaqzzjg",  # 有无安全组织架构
        "description": "本次任务有无安全组织架构",
        "suggestion": "1.提前建立安全组织架构",
        "risk_matrix": {
            0: {"possibility": 7, "severity": 6},  # 无
            1: {"possibility": 2, "severity": 2}   # 有
        }
    },
    "indicator_030": {
        "index_number": 30,
        "level_1": "管理因素",
        "level_2": "管理组织",
        "level_3": "组织职责是否明确",
        "pinyin_code": "zzzrsfmq",  # 组织职责是否明确
        "description": "组织职责是否明确",
        "suggestion": "1.提前明确组织职责",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 5},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_031": {
        "index_number": 31,
        "level_1": "管理因素",
        "level_2": "管理制度",
        "level_3": "是否开展教育训练",
        "pinyin_code": "sfkzjyxl",  # 是否开展教育训练
        "description": "是否开展教育训练",
        "suggestion": "1.提前开展教育训练",
        "risk_matrix": {
            0: {"possibility": 5, "severity": 4},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_032": {
        "index_number": 32,
        "level_1": "管理因素",
        "level_2": "管理制度",
        "level_3": "有无安全制度",
        "pinyin_code": "ywaqzd",  # 有无安全制度
        "description": "有无安全制度",
        "suggestion": "1.提前准备安全制度",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 5},  # 无
            1: {"possibility": 2, "severity": 2}   # 有
        }
    },
    "indicator_033": {
        "index_number": 33,
        "level_1": "管理因素",
        "level_2": "管理制度",
        "level_3": "有无安全预案",
        "pinyin_code": "ywaqya",  # 有无安全预案
        "description": "有无安全预案",
        "suggestion": "1.提前准备安全预案",
        "risk_matrix": {
            0: {"possibility": 7, "severity": 6},  # 无
            1: {"possibility": 2, "severity": 2}   # 有
        }
    },
    "indicator_034": {
        "index_number": 34,
        "level_1": "管理因素",
        "level_2": "管理制度",
        "level_3": "有无安全设施",
        "pinyin_code": "ywaqss",  # 有无安全设施
        "description": "有无安全设施",
        "suggestion": "1.提前准备安全设施",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 6},  # 无
            1: {"possibility": 2, "severity": 2}   # 有
        }
    },
    "indicator_035": {
        "index_number": 35,
        "level_1": "管理因素",
        "level_2": "管理制度",
        "level_3": "是否通过弹药结构安全性技术检查",
        "pinyin_code": "sftgdyjgaqqxjsjc",  # 是否通过弹药结构安全性技术检查
        "description": "是否经过弹药结构安全性技术检查",
        "suggestion": "1.提前经过弹药结构安全性技术检查",
        "risk_matrix": {
            0: {"possibility": 8, "severity": 7},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_036": {
        "index_number": 36,
        "level_1": "管理因素",
        "level_2": "管理机制",
        "level_3": "是否经过安全分析",
        "pinyin_code": "sfjgaqfx",  # 是否经过安全分析
        "description": "是否经过安全分析",
        "suggestion": "1.提前进行专家安全分析",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 5},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_037": {
        "index_number": 37,
        "level_1": "管理因素",
        "level_2": "管理机制",
        "level_3": "是否经过专家评审",
        "pinyin_code": "sfjgzjps",  # 是否经过专家评审
        "description": "是否经过专家评审",
        "suggestion": "1.提前进行专家评审",
        "risk_matrix": {
            0: {"possibility": 5, "severity": 4},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_038": {
        "index_number": 38,
        "level_1": "管理因素",
        "level_2": "管理机制",
        "level_3": "有无风险预警",
        "pinyin_code": "ywfxyj",  # 有无风险预警
        "description": "有无风险预警",
        "suggestion": "1.提前准备风险预警",
        "risk_matrix": {
            0: {"possibility": 6, "severity": 5},  # 无
            1: {"possibility": 2, "severity": 2}   # 有
        }
    },
    "indicator_039": {
        "index_number": 39,
        "level_1": "管理因素",
        "level_2": "管理机制",
        "level_3": "有协调联动机制",
        "pinyin_code": "yxtldjz",  # 有协调联动机制
        "description": "有无与相关部门的协调联动机制",
        "suggestion": "1.提前协调联动有关部门",
        "risk_matrix": {
            0: {"possibility": 5, "severity": 4},  # 无
            1: {"possibility": 2, "severity": 2}   # 有
        }
    },
    "indicator_040": {
        "index_number": 40,
        "level_1": "管理因素",
        "level_2": "管理能力",
        "level_3": "有无计划统筹",
        "pinyin_code": "ywjhtc",  # 有无计划统筹
        "description": "有无计划统筹",
        "suggestion": "1.提前计划统筹本次任务",
        "risk_matrix": {
            0: {"possibility": 5, "severity": 4},  # 无
            1: {"possibility": 2, "severity": 2}   # 有
        }
    },
    "indicator_041": {
        "index_number": 41,
        "level_1": "管理因素",
        "level_2": "管理能力",
        "level_3": "是否贯彻落实",
        "pinyin_code": "sfgcls",  # 是否贯彻落实
        "description": "是否贯彻落实形成管理能力的相关工作",
        "suggestion": "1.提前贯彻落实本次任务",
        "risk_matrix": {
            0: {"possibility": 5, "severity": 4},  # 否
            1: {"possibility": 2, "severity": 2}   # 是
        }
    },
    "indicator_042": {
        "index_number": 42,
        "level_1": "管理因素",
        "level_2": "管理能力",
        "level_3": "有无应急处置",
        "pinyin_code": "ywyjcz",  # 有无应急处置
        "description": "有无应急处置能力及相关设备",
        "suggestion": "1.提前准备应急处置措施",
        "risk_matrix": {
            0: {"possibility": 7, "severity": 6},  # 无
            1: {"possibility": 2, "severity": 2}   # 有
        }
    },
    "indicator_043": {
        "index_number": 43,
        "level_1": "任务因素",
        "level_2": "任务性质",
        "level_3": "是否为特殊任务",
        "pinyin_code": "sfwtsrw",  # 是否为特殊任务
        "description": "是否为特殊任务",
        "suggestion": "1.特殊任务需要特殊对待",
        "risk_matrix": {
            0: {"possibility": 3, "severity": 3},  # 否
            1: {"possibility": 6, "severity": 6}   # 是
        }
    },
    "indicator_044": {
        "index_number": 44,
        "level_1": "任务因素",
        "level_2": "任务性质",
        "level_3": "是否为紧急任务",
        "pinyin_code": "sfwjjrw",  # 是否为紧急任务
        "description": "是否为紧急任务",
        "suggestion": "1.保证不出错的前提下适当加快车速",
        "risk_matrix": {
            0: {"possibility": 3, "severity": 3},  # 否
            1: {"possibility": 7, "severity": 5}   # 是
        }
    },
    "indicator_045": {
        "index_number": 45,
        "level_1": "任务因素",
        "level_2": "任务强度",
        "level_3": "任务时长（天）",
        "pinyin_code": "rwsc",  # 任务时长
        "description": "任务时长",
        "suggestion": "1.大于一天的任务夜间休息时注意警戒",
        "risk_matrix": {
            0: {"possibility": 2, "severity": 3},  # 1天以内
            1: {"possibility": 4, "severity": 4},  # 1-3天
            2: {"possibility": 6, "severity": 5},  # 3-7天
            3: {"possibility": 7, "severity": 6}   # 7天以上
        }
    }
}

# 拼音编码到indicator_xxx的映射表，用于支持两种输入格式
PINYIN_TO_INDICATOR = {}
for indicator_id, config in INDICATORS_CONFIG.items():
    pinyin_code = config.get("pinyin_code")
    if pinyin_code:
        PINYIN_TO_INDICATOR[pinyin_code] = indicator_id

# 风险等级判定标准
RISK_LEVELS = {
    (0, 20): "一般",
    (21, 41): "较大", 
    (42, 69): "重大",
    (70, 100): "特大"
}

# 敏感度指标系数配置
SENSITIVITY_CONFIG = {
    "sensitive_time": {
        "description": "敏感时期",
        "examples": "重大节假日、外事活动、赛事、重要会议、庆祝活动、纪念活动",
        "options": {
            0: "否",
            1: "是"
        }
    },
    "sensitive_area": {
        "description": "敏感地域", 
        "examples": "边境、争议海空域、少数民族聚居地",
        "options": {
            0: "否",
            1: "是"
        }
    },
    "sensitive_attribute": {
        "description": "敏感属性",
        "examples": "弹药运输、战略演习、重大危险源、新域新质作战力量重要活动、高等级涉密事项",
        "options": {
            0: "一般",
            1: "较大", 
            2: "重大"
        }
    }
}

# 指标权重配置 - 根据表4风险计算及指标权重表（参考）
INDICATOR_WEIGHTS = {
    # 人员因素 - 根据表4综合权重
    "indicator_001": 2.5,   # 岗位种类是否齐全
    "indicator_002": 2.5,   # 主要岗位任职年限是否超5年
    "indicator_003": 1.25,  # 是否存在一人多岗
    "indicator_004": 5.25,  # 共产党员占比
    "indicator_005": 3.5,   # 是否全部通过政治审查
    "indicator_006": 4,     # 是否全部参加过安全教育
    "indicator_007": 2,     # 是否全部参加过保密培训
    "indicator_008": 2,     # 实操技能考核是否全部通过
    "indicator_009": 2,     # 理论知识考核是否全部通过
    
    # 物品因素 - 暂定为1（未在表中给出具体数值）
    "indicator_010": 1,     # 弹药类型
    "indicator_011": 1,     # 弹药质量等级
    "indicator_012": 1,     # 弹药重量
    "indicator_013": 1,     # 弹药数量
    "indicator_014": 1,     # 设备是否齐全
    "indicator_015": 1,     # 设备状况是否良好
    "indicator_016": 1,     # 车辆状况
    "indicator_017": 1,     # 车辆安全配套设备
    "indicator_018": 1,     # 车辆数量
    
    # 环境因素 - 暂定为1（未在表中给出具体数值）
    "indicator_019": 1,     # 道路类型
    "indicator_020": 1,     # 运输距离
    "indicator_021": 1,     # 是否有备用路线
    "indicator_022": 1,     # 是否经过重点保护区域
    "indicator_023": 1,     # 季节
    "indicator_024": 1,     # 特殊天气
    "indicator_025": 1,     # 社情民情
    "indicator_026": 1,     # 敌情
    "indicator_027": 1,     # 保密工作是否到位
    
    # 管理因素 - 暂定为1（未在表中给出具体数值）
    "indicator_028": 1,     # 领导组织机构是否建立
    "indicator_029": 1,     # 有无安全组织架构
    "indicator_030": 1,     # 组织职责是否明确
    "indicator_031": 1,     # 是否开展教育训练
    "indicator_032": 1,     # 有无安全制度
    "indicator_033": 1,     # 有无安全预案
    "indicator_034": 1,     # 有无安全设施
    "indicator_035": 1,     # 是否通过弹药结构安全性技术检查
    "indicator_036": 1,     # 是否经过安全分析
    "indicator_037": 1,     # 是否经过专家评审
    "indicator_038": 1,     # 有无风险预警
    "indicator_039": 1,     # 有协调联动机制
    "indicator_040": 1,     # 有无计划统筹
    "indicator_041": 1,     # 是否贯彻落实
    "indicator_042": 1,     # 有无应急处置
    
    # 任务因素 - 暂定为1（未在表中给出具体数值）
    "indicator_043": 1,     # 是否为特殊任务
    "indicator_044": 1,     # 是否为紧急任务
    "indicator_045": 1      # 任务时长
}

def get_sensitivity_coefficient(sensitive_time, sensitive_area, sensitive_attribute):
    """
    根据敏感度指标获取敏感度系数
    按照表2敏感度指标系数表进行计算
    """
    # 等级5：敏感时期是 + 敏感地域是 + 敏感属性重大
    if sensitive_time == 1 and sensitive_area == 1 and sensitive_attribute == 2:
        return 2.0
    
    # 等级4：三种情况
    # 敏感时期是 + 敏感地域是 + 敏感属性较大
    if sensitive_time == 1 and sensitive_area == 1 and sensitive_attribute == 1:
        return 1.75
    # 敏感时期是 + 敏感属性重大
    if sensitive_time == 1 and sensitive_attribute == 2:
        return 1.75
    # 敏感地域是 + 敏感属性重大  
    if sensitive_area == 1 and sensitive_attribute == 2:
        return 1.75
    
    # 等级3：四种情况
    # 敏感时期是 + 敏感地域是
    if sensitive_time == 1 and sensitive_area == 1:
        return 1.5
    # 敏感时期是 + 敏感属性较大
    if sensitive_time == 1 and sensitive_attribute == 1:
        return 1.5
    # 敏感地域是 + 敏感属性较大
    if sensitive_area == 1 and sensitive_attribute == 1:
        return 1.5
    # 敏感属性重大
    if sensitive_attribute == 2:
        return 1.5
    
    # 等级2：三种情况
    # 敏感时期是
    if sensitive_time == 1:
        return 1.25
    # 敏感地域是
    if sensitive_area == 1:
        return 1.25
    # 敏感属性较大
    if sensitive_attribute == 1:
        return 1.25
    
    # 等级1：敏感时期否 + 敏感地域否 + 敏感属性一般
    return 1.0

def get_indicator_weight(indicator_id):
    """获取指标权重"""
    return INDICATOR_WEIGHTS.get(indicator_id, 1.0)  # 默认权重1.0

def calculate_comprehensive_risk(detail_risks, sensitivity_coefficient=1.0):
    """
    使用综合风险计算公式：α = k(1+l/50)∑(wi*ri)
    
    参数:
        detail_risks: 详细风险信息字典
        sensitivity_coefficient: 敏感度系数k
        
    返回:
        tuple: (风险等级, 风险值)
    """
    if not detail_risks:
        return "无风险", 0
    
    # 获取指标数量l
    l = len(detail_risks)
    
    # 计算加权风险值总和 ∑(wi*ri)
    weighted_risk_sum = 0
    for indicator_name, risk_info in detail_risks.items():
        # 通过level_3匹配找到对应的indicator_id
        indicator_id = None
        for ind_id, config in INDICATORS_CONFIG.items():
            if config["level_3"] == indicator_name:
                indicator_id = ind_id
                break
        
        if indicator_id:
            wi = get_indicator_weight(indicator_id)  # 权重wi
            ri = int(risk_info[2])  # 风险值ri（在索引2位置）
            weighted_risk_sum += wi * ri
    
    # 应用公式：α = k(1+l/50)∑(wi*ri)
    quantity_factor = 1 + l / 50  # 数量修正因子(1+l/50)
    alpha = sensitivity_coefficient * quantity_factor * weighted_risk_sum
    
    # 限制在合理范围内[0, 100]
    adjusted_risk = min(100, max(0, int(alpha)))
    
    # 确定风险等级
    risk_level = get_risk_level(adjusted_risk)
    
    return risk_level, adjusted_risk

def get_risk_level(risk_value):
    """根据风险值确定风险等级"""
    for (min_val, max_val), level in RISK_LEVELS.items():
        if min_val <= risk_value <= max_val:
            return level
    return "未知风险"

def calculate_overall_risk(detail_risks, sensitivity_coefficient=1.0):
    """计算总体风险等级，使用综合风险计算公式"""
    return calculate_comprehensive_risk(detail_risks, sensitivity_coefficient) 