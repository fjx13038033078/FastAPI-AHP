"""
API路由定义
"""
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import logging

from ..models.schemas import IndicatorData, RiskEvaluationResponse
from ..services.risk_evaluator import RiskEvaluator
from ..utils.indicators import INDICATORS_CONFIG, PINYIN_TO_INDICATOR, SENSITIVITY_CONFIG, INDICATOR_WEIGHTS

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

@router.get("/indicators/mapping", response_model=Dict[str, Any])
async def get_pinyin_mapping():
    """
    获取拼音编码到indicator_xxx的映射表
    
    返回:
        Dict: 拼音编码映射表
    """
    try:
        response = {
            "code": 200,
            "message": "ok", 
            "data": {
                "pinyin_to_indicator": PINYIN_TO_INDICATOR,
                "mapping_count": len(PINYIN_TO_INDICATOR)
            }
        }
        
        logger.info(f"返回拼音编码映射表，共 {len(PINYIN_TO_INDICATOR)} 个映射")
        return response
        
    except Exception as e:
        logger.error(f"获取拼音编码映射失败: {str(e)}")
        raise HTTPException(status_code=500, detail=f"获取拼音编码映射失败: {str(e)}")

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

@router.get("/indicators/sensitivity", response_model=Dict[str, Any])
async def get_sensitivity_indicators():
    """
    获取敏感度指标信息
    
    返回:
        Dict: 包含敏感度指标配置信息
    """
    try:
        response = {
            "code": 200,
            "message": "ok",
            "data": {
                "sensitivity_config": SENSITIVITY_CONFIG,
                "description": "敏感度指标用于调整基础风险值，系数范围1.0-2.0",
                "coefficient_levels": {
                    "等级1": {"conditions": "敏感时期否 + 敏感地域否 + 敏感属性一般", "coefficient": 1.0},
                    "等级2": {"conditions": "敏感时期是 或 敏感地域是 或 敏感属性较大", "coefficient": 1.25},
                    "等级3": {"conditions": "敏感时期是+敏感地域是 或 敏感时期是+敏感属性较大 或 敏感地域是+敏感属性较大 或 敏感属性重大", "coefficient": 1.5},
                    "等级4": {"conditions": "敏感时期是+敏感地域是+敏感属性较大 或 敏感时期是+敏感属性重大 或 敏感地域是+敏感属性重大", "coefficient": 1.75},
                    "等级5": {"conditions": "敏感时期是 + 敏感地域是 + 敏感属性重大", "coefficient": 2.0}
                },
                "usage": {
                    "sensitive_time": "敏感时期：0-否，1-是",
                    "sensitive_area": "敏感地域：0-否，1-是", 
                    "sensitive_attribute": "敏感属性：0-一般，1-较大，2-重大"
                },
                "formula": "综合风险计算公式: α = k(1+l/50)∑(wi*ri)"
            }
        }
        
        logger.info("返回敏感度指标信息")
        return response
        
    except Exception as e:
        logger.error(f"获取敏感度指标信息失败: {str(e)}")
        raise HTTPException(status_code=500, detail=f"获取敏感度指标信息失败: {str(e)}")

@router.get("/indicators/weights", response_model=Dict[str, Any])
async def get_indicator_weights():
    """
    获取指标权重信息
    
    返回:
        Dict: 包含所有指标的权重配置
    """
    try:
        # 按类别组织权重信息
        weights_by_category = {}
        for indicator_id, weight in INDICATOR_WEIGHTS.items():
            if indicator_id in INDICATORS_CONFIG:
                config = INDICATORS_CONFIG[indicator_id]
                category = config["level_1"]
                
                if category not in weights_by_category:
                    weights_by_category[category] = {}
                
                weights_by_category[category][indicator_id] = {
                    "weight": weight,
                    "name": config["level_3"],
                    "description": config["description"],
                    "index_number": config["index_number"]
                }
        
        response = {
            "code": 200,
            "message": "ok",
            "data": {
                "weights_by_category": weights_by_category,
                "total_indicators": len(INDICATOR_WEIGHTS),
                "description": "指标权重用于综合风险计算公式中的wi参数",
                "formula": "α = k(1+l/50)∑(wi*ri)",
                "weight_explanation": {
                    "范围": "0.4-1.0",
                    "含义": "数值越高表示指标越重要",
                    "分类": {
                        "物品因素": "权重最高(0.6-1.0)，特别是弹药和车辆相关",
                        "人员因素": "权重较高(0.6-0.9)，特别是岗位和技能相关", 
                        "环境因素": "权重中等(0.4-1.0)，敌情和重点区域权重高",
                        "管理因素": "权重中等(0.5-0.8)，安全制度和应急处置重要",
                        "任务因素": "权重较高(0.6-0.8)，特殊任务权重高"
                    }
                }
            }
        }
        
        logger.info(f"返回指标权重信息，共 {len(INDICATOR_WEIGHTS)} 个指标")
        return response
        
    except Exception as e:
        logger.error(f"获取指标权重信息失败: {str(e)}")
        raise HTTPException(status_code=500, detail=f"获取指标权重信息失败: {str(e)}") 