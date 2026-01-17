from fastapi import APIRouter
from app.core.pipeline_state import get_state
from app.services.llm_explainer import explain_anomalies

router = APIRouter(prefix="/explain", tags=["LLM Explainer"])

@router.post("/")
def explain():
    anomalies = get_state("anomalies", [])
    
    return explain_anomalies(anomalies)