from fastapi import APIRouter
from app.services.llm_explainer import explain_anomalies

router = APIRouter(prefix="/explain", tags=["LLM Explainer"])

@router.post("/")
def explain(anomalies: list):
    # placeholder for LLM client for now
    explanations = explain_anomalies(
        anomalies=anomalies,
        llm_client=lambda prompt: "This is a placeholder explanation from the LLM."
    )
    return explanations