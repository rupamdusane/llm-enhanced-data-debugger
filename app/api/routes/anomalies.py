from fastapi import APIRouter, HTTPException
from app.core.datastore import datastore
from app.services.anomaly_detector import detect_anomalies

router = APIRouter(prefix="/anomalies", tags=["Anomalies"])

@router.post("/")
def analyze_anomalies():
    try:
        df = datastore.get_dataframe()
        anomalies = detect_anomalies(df)
        
        return {"anomalies": anomalies}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))