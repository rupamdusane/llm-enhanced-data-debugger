from fastapi import APIRouter, HTTPException
from app.core.datastore import datastore
from app.services.inspection_services import inspect_dataframe
from app.core.pipeline_state import set_state

router = APIRouter()

@router.post("/inspect")
def inspect_file():
    try:
        df = datastore.get_dataframe()
        if df is None:
            raise ValueError("No dataset uploaded.")
        
        inspection_result = inspect_dataframe(df)

        set_state("inspection", inspection_result)

        return inspection_result
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))