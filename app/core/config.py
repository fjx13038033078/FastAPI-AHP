"""
应用配置
"""
import os
from typing import Optional

class Settings:
    """应用设置"""
    
    # 应用基本信息
    APP_NAME: str = "AHP风险评估系统"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "基于AHP方法的安全风险评估系统"
    
    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # 文件路径配置
    REPORTS_DIR: str = "reports"
    DOCS_DIR: str = "docs"
    
    # API配置
    API_PREFIX: str = "/api"
    
    def __init__(self):
        """初始化配置，确保必要的目录存在"""
        os.makedirs(self.REPORTS_DIR, exist_ok=True)
        os.makedirs(self.DOCS_DIR, exist_ok=True)

# 全局配置实例
settings = Settings() 