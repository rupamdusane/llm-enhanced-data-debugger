from fastapi import APIRouter, HTTPException
from app.core.datastore import datastore
from app.services.inspection_services import inspect_dataframe

router = APIRouter()

@router.post("/inspect")
def inspect_file():
    try:
        df = datastore.get_dataframe()
        if df is None:
            raise ValueError("No dataset uploaded.")
        
        return inspect_dataframe(df)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))