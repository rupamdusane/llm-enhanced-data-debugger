from fastapi import APIRouter
from app.services.anomaly_detector import detect_anolamiles

router = APIRouter(prefix="/anomalies", tags=["Anomalies"])

@router.post("/")
def analyze_anomalies(inspeciton_result: dict):
    anomalies = detect_anolamiles(inspeciton_result)
    
    return {
        "anomalies": anomalies
    }