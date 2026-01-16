from fastapi import APIRouter, HTTPException
from app.services.explanation_service import explain_anomalies

router = APIRouter(prefix="/explain", tags=["LLM Explainer"])

@router.post("/")
def explain():
    try:
        return explain_anomalies()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))