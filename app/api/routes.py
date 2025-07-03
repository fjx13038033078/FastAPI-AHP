"""
API路由定义
"""
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import logging

from ..models.schemas import IndicatorData, RiskEvaluationResponse
from ..services.risk_evaluator import RiskEvaluator
from ..utils.indicators import INDICATORS_CONFIG

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建路由器
router = APIRouter()

# 初始化风险评估器
risk_evaluator = RiskEvaluator()

@router.get("/indicators", response_model=Dict[str, Any])
async def get_indicators():
    """
    获取所有指标信息
    
    返回:
        Dict: 包含所有指标的信息，包括拼音编码
    """
    try:
        indicators_info = {}
        for key, config in INDICATORS_CONFIG.items():
            indicators_info[key] = {
                "index_number": config["index_number"],
                "level_1": config["level_1"],
                "level_2": config["level_2"],
                "level_3": config["level_3"],
                "pinyin_code": config.get("pinyin_code", ""),
                "description": config["description"],
                "suggestion": config["suggestion"]
            }
        
        response = {
            "code": 200,
            "message": "ok",
            "data": indicators_info
        }
        
        logger.info(f"返回指标信息，共 {len(indicators_info)} 个指标")
        return response
        
    except Exception as e:
        logger.error(f"获取指标信息失败: {str(e)}")
        raise HTTPException(status_code=500, detail=f"获取指标信息失败: {str(e)}")



@router.post("/risk/evaluate", response_model=RiskEvaluationResponse)
async def evaluate_risk(data: IndicatorData):
    """
    风险评估接口
    支持两种输入格式：
    1. indicator_xxx格式（如：indicator_001）
    2. 拼音编码格式（如：gwzlsfqq）
    
    参数:
        data: 指标数据
        
    返回:
        RiskEvaluationResponse: 风险评估结果
    """
    try:
        # 执行风险评估
        result = risk_evaluator.evaluate(data)
        
        response = RiskEvaluationResponse(
            code=200,
            message="ok",
            data=result
        )
        
        logger.info(f"风险评估完成，总体风险等级: {result.get('level', 'Unknown')}")
        return response
        
    except Exception as e:
        logger.error(f"风险评估失败: {str(e)}")
        raise HTTPException(status_code=500, detail=f"风险评估失败: {str(e)}")

@router.get("/health")
async def health_check():
    """健康检查接口"""
    return {
        "status": "healthy",
        "message": "AHP风险评估系统运行正常",
        "version": "1.0.0"
    }



 