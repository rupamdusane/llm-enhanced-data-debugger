from pydantic import BaseModel
from typing import List

class ExplanationItem(BaseModel):
    anomaly_type: str
    column: str
    explanaiton: str
    
class ExplanationResponse(BaseModel):
    summary: str
    explanations: List[ExplanationItem]