from fastapi import APIRouter

router = APIRouter()

@router.get("/anomalies")
def anomalies_placeholder():
    return {"status": "anomalies module placeholder"}
