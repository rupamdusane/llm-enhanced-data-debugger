from fastapi import APIRouter
from app.services.explanation_service import explain_anomalies
from app.core.pipeline_guard import require_state

router = APIRouter(prefix="/explain", tags=["LLM Explainer"])

@router.post("/")
def explain():
    require_state("anomalies")
    return explain_anomalies()