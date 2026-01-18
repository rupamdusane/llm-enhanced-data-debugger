from fastapi import APIRouter, HTTPException
from app.services.anomaly_detector import detect_anomalies
from app.core.pipeline_state import get_state
from app.core.pipeline_guard import require_state

router = APIRouter(prefix="/anomalies", tags=["Anomalies"])

@router.post("/")
def analyze_anomalies():
    require_state("inspection")
    
    inspection_result = get_state("inspection")
    anomalies = detect_anomalies(inspection_result)
    
    return {"anomalies": anomalies}