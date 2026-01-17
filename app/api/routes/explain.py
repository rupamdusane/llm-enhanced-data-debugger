from fastapi import APIRouter
from app.services.explanation_service import explain_anomalies
from app.schemas.explanation import ExplanationResponse

router = APIRouter(prefix="/explain", tags=["LLM Explainer"])

@router.post("/", response_model=ExplanationResponse)
def explain():
    return explain_anomalies()