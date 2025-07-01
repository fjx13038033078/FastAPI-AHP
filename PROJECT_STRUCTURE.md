# AHP风险评估系统 - 项目结构说明

## 项目结构

经过重构后，项目采用了标准的Python项目结构，便于维护和扩展：

```
fastApiProject/
├── app/                           # 主应用包
│   ├── __init__.py               # 应用包初始化
│   ├── main.py                   # FastAPI应用入口
│   ├── core/                     # 核心配置模块
│   │   ├── __init__.py
│   │   └── config.py             # 应用配置
│   ├── api/                      # API路由模块
│   │   ├── __init__.py
│   │   └── routes.py             # API路由定义
│   ├── models/                   # 数据模型模块
│   │   ├── __init__.py
│   │   └── schemas.py            # Pydantic数据模型
│   ├── services/                 # 业务逻辑服务模块
│   │   ├── __init__.py
│   │   ├── risk_evaluator.py     # 风险评估服务
│   │   └── pdf_generator.py      # PDF生成服务
│   └── utils/                    # 工具函数模块
│       ├── __init__.py
│       └── indicators.py         # 指标配置
├── tests/                        # 测试文件目录
│   ├── test_refactored.py        # 重构后的测试
│   ├── test_modules.py           # 模块测试
│   ├── test_api.py               # API测试
│   └── test_quick.py             # 快速测试
├── config/                       # 外部配置目录
├── reports/                      # 生成的PDF报告
├── docs/                         # 文档目录
├── run.py                        # 项目启动文件
├── requirements.txt              # 项目依赖
├── Dockerfile                    # Docker镜像构建文件
├── docker-compose.yml            # Docker编排文件
└── README.md                     # 项目说明
```

## 模块说明

### 1. 核心模块 (app/core/)
- `config.py`: 应用配置管理，包含服务器设置、路径配置等

### 2. API模块 (app/api/)
- `routes.py`: 定义所有API路由，包括指标查询和风险评估接口

### 3. 数据模型 (app/models/)
- `schemas.py`: Pydantic数据模型，定义请求和响应的数据结构

### 4. 服务模块 (app/services/)
- `risk_evaluator.py`: 风险评估核心逻辑
- `pdf_generator.py`: PDF报告生成服务

### 5. 工具模块 (app/utils/)
- `indicators.py`: 指标配置和风险评估矩阵

### 6. 测试模块 (tests/)
- 包含各种测试文件，确保代码质量

## 启动方式

### 1. 开发环境启动
```bash
python run.py
```

### 2. 模块导入启动
```bash
python -m app.main
```

### 3. Uvicorn直接启动
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Docker启动
```bash
docker-compose up -d
```

## API接口

### 健康检查
- **GET** `/health`
- **GET** `/api/health`

### 指标信息
- **GET** `/api/indicators`

### 风险评估
- **POST** `/api/risk/evaluate`

## 项目优势

1. **模块化设计**: 清晰的模块分离，便于维护和扩展
2. **标准结构**: 符合Python项目最佳实践
3. **配置管理**: 集中的配置管理，便于部署
4. **测试完整**: 完整的测试覆盖，保证代码质量
5. **文档完善**: 详细的文档说明，便于新人上手

## 扩展说明

### 添加新的API接口
1. 在 `app/api/routes.py` 中添加新的路由
2. 在 `app/models/schemas.py` 中定义相关数据模型
3. 在相应的服务模块中实现业务逻辑

### 添加新的服务
1. 在 `app/services/` 目录下创建新的服务文件
2. 在路由中导入并使用新服务

### 添加新的配置
1. 在 `app/core/config.py` 中添加配置项
2. 在需要的地方导入并使用配置

这种结构设计使得项目更加规范化、模块化，便于团队协作和后续维护扩展。 