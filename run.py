"""
AHP风险评估系统启动文件
"""
import uvicorn
from app.main import app
from app.core.config import settings

if __name__ == "__main__":
    print(f"🚀 启动 {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"📍 服务地址: http://{settings.HOST}:{settings.PORT}")
    print(f"📖 API文档: http://{settings.HOST}:{settings.PORT}/docs")
    print(f"📗 ReDoc文档: http://{settings.HOST}:{settings.PORT}/redoc")
    
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    ) 