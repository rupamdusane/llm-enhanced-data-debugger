from fastapi import APIRouter, HTTPException
from app.services.anomaly_detector import detect_anomalies
from app.core.pipeline_state import pipeline_state, set_state, get_state

router = APIRouter(prefix="/anomalies", tags=["Anomalies"])

@router.post("/")
def analyze_anomalies():
    try:
        inspection_result = get_state("inspection")
        if inspection_result is None:
            raise ValueError("Inspection has not been run")

        anomalies = detect_anomalies(inspection_result)
        return {"anomalies": anomalies}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))