from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class BasicInfo(BaseModel):
    rwmc: str
    pgdwmc: str

class SensitivityInfo(BaseModel):
    """敏感度信息"""
    sensitive_time: int = 0      # 敏感时期：0-否，1-是
    sensitive_area: int = 0      # 敏感地域：0-否，1-是 
    sensitive_attribute: int = 0 # 敏感属性：0-一般，1-较大，2-重大

class IndicatorData(BaseModel):
    jcxx: BasicInfo
    zbxx: Dict[str, Any]
    mgdxx: Optional[SensitivityInfo] = None  # 敏感度信息，可选

class RiskDetail(BaseModel):
    level: str
    detail: Dict[str, List[str]]
    report_time: str = None
    rwmc: str
    dwmc: str
    filePath: str

class RiskResponse(BaseModel):
    msg: str
    code: str
    data: RiskDetail

class IndicatorInfo(BaseModel):
    id: str
    name: str
    description: str
    category: str
    index_number: str

class RiskEvaluationResponse(BaseModel):
    code: int
    message: str
    data: Dict[str, Any] 