# AHP风险评估系统

基于AHP（层次分析法）的风险评估系统，支持45个风险指标的综合评估和PDF报告生成。

## 🎯 系统特性

- ✅ **完整的45指标体系**：覆盖人员、物品、环境、管理、任务五大因素
- ✅ **智能风险评估**：基于AHP算法的科学风险评估
- ✅ **PDF报告生成**：自动生成标准格式的风险评估报告
- ✅ **中文字体支持**：完美显示中文内容
- ✅ **RESTful API**：标准化的HTTP接口
- ✅ **模块化架构**：易于维护和扩展

## 📊 指标体系

### 人员因素 (9个指标)
- **岗位相关** (3个)：岗位种类齐全性、任职年限、一人多岗情况
- **政治素质** (2个)：共产党员占比、政治审查通过情况
- **业务素质** (4个)：安全教育、保密培训、实操技能、理论知识

### 物品因素 (9个指标)
- **弹药相关** (4个)：弹药类型、质量等级、重量、数量
- **机工具** (2个)：设备齐全性、设备状况
- **运输车辆** (3个)：车辆状况、安全配套设备、车辆数量

### 环境因素 (9个指标)
- **道路相关** (4个)：道路类型、运输距离、备用路线、保护区域
- **天气相关** (2个)：季节、特殊天气
- **社会因素** (3个)：社情民情、敌情、保密工作

### 管理因素 (15个指标)
- **管理组织** (3个)：领导组织机构、安全组织架构、组织职责
- **管理制度** (5个)：教育训练、安全制度、安全预案、安全设施、技术检查
- **管理机制** (4个)：安全分析、专家评审、风险预警、协调联动
- **管理能力** (3个)：计划统筹、贯彻落实、应急处置

### 任务因素 (3个指标)
- **任务性质** (2个)：特殊任务、紧急任务
- **任务强度** (1个)：任务时长

## 🚀 快速开始

### 1. 环境要求
```bash
Python 3.8+
FastAPI
ReportLab
Uvicorn
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 启动服务
```bash
# 方式1：使用启动脚本
python run.py

# 方式2：直接使用uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. 访问API
- 服务地址：`http://localhost:8000`
- API文档：`http://localhost:8000/docs`
- 健康检查：`http://localhost:8000/api/health`

## 📡 API接口

### 1. 获取指标信息
```http
GET /api/indicators
```

**响应示例：**
```json
{
    "code": 200,
    "message": "ok",
    "data": {
        "indicator_001": {
            "index_number": 1,
            "level_1": "人员因素",
            "level_2": "岗位",
            "level_3": "岗位种类是否齐全",
            "description": "管理干部、库房管理员、作业人员、警戒员、安全员、驾驶员是否齐全",
            "suggestion": "1.确定缺失哪类岗位\n2.补充缺失的岗位人员"
        }
        // ... 其他44个指标
    }
}
```

### 2. 风险评估
```http
POST /api/risk/evaluate
```

**请求体：**
```json
{
    "jcxx": {
        "rwmc": "任务名称",
        "pgdwmc": "派遣单位名称"
    },
    "zbxx": {
        "indicator_001": "1",
        "indicator_002": "0",
        // ... 其他指标值
    }
}
```

**响应示例：**
```json
{
    "code": 200,
    "message": "ok",
    "data": {
        "level": "一般风险",
        "detail": {
            "indicator_001": ["岗位种类是否齐全", "轻微风险", "4", "1.确定缺失哪类岗位\n2.补充缺失的岗位人员"]
            // ... 其他指标详情
        },
        "report_time": "2024-01-15 14:30:00",
        "rwmc": "任务名称",
        "dwmc": "派遣单位名称",
        "filePath": "reports/risk_report_xxxxx.pdf"
    }
}
```

## 🎨 风险等级说明

| 风险值范围 | 风险等级 | 可容许性 | 颜色标识 |
|-----------|---------|---------|---------|
| R<21      | 一般    | 可接受   | 绿色    |
| 21≤R<42   | 较大    | 中间     | 黄色    |
| 42≤R<70   | 重大    | 中间     | 橙色    |
| 70≤R≤100  | 特大    | 不可接受 | 红色    |

**风险值计算公式：** 风险值 = 可能性等级 × 严重程度等级

## 📁 项目结构

```
fastApiProject/
├── app/                           # 主应用包
│   ├── __init__.py
│   ├── main.py                    # FastAPI应用入口
│   │   ├── __init__.py
│   │   └── routes.py              # API路由定义
│   ├── core/                      # 核心配置模块
│   │   ├── __init__.py
│   │   └── config.py              # 应用配置
│   ├── models/                    # 数据模型模块
│   │   ├── __init__.py
│   │   └── schemas.py             # Pydantic数据模型
│   ├── services/                  # 业务逻辑服务模块
│   │   ├── __init__.py
│   │   ├── risk_evaluator.py      # 风险评估服务
│   │   └── pdf_generator.py       # PDF生成服务
│   └── utils/                     # 工具函数模块
│       ├── __init__.py
│       └── indicators.py          # 指标配置
├── tests/                         # 测试文件目录
│   ├── test_system.py             # 系统测试
│   └── test_all_indicators.py     # 指标测试
├── config/                        # 外部配置目录
├── reports/                       # 生成的PDF报告
├── run.py                         # 项目启动文件
├── requirements.txt               # 项目依赖
├── Dockerfile                     # Docker配置
├── docker-compose.yml             # Docker Compose配置
└── README.md                      # 项目说明
```

## 🧪 测试

### 运行所有测试
```bash
pytest tests/ -v
```

### 运行指标配置测试
```bash
pytest tests/test_all_indicators.py::test_all_indicators_configured -v
```

### 运行API测试
```bash
pytest tests/test_system.py -v
```

## 🐳 Docker部署

### 1. 构建镜像
```bash
docker build -t ahp-risk-system .
```

### 2. 运行容器
```bash
docker run -p 8000:8000 ahp-risk-system
```

### 3. 使用Docker Compose
```bash
docker-compose up -d
```

## 📊 指标配置说明

所有45个指标都已完整配置，每个指标包含：

- **基本信息**：序号、分类层级、名称、描述
- **风险矩阵**：不同输入值对应的可能性和严重程度等级
- **对策建议**：针对性的风险应对措施

详细的指标配置参见 `指标数据模板.md` 文件。

## 🔧 自定义配置

### 修改指标配置
编辑 `app/utils/indicators.py` 文件中的 `INDICATORS_CONFIG` 字典。

### 调整风险等级
修改 `app/utils/indicators.py` 文件中的 `RISK_LEVELS` 配置。

### 自定义PDF模板
修改 `app/services/pdf_generator.py` 文件中的PDF生成逻辑。

---

**注意：** 此系统已完整实现45个风险指标的评估功能，所有模块均已测试通过，可直接投入生产使用。 
