from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

from app.core.datastore import datastore
from app.core.pipeline_state import clear_state

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        #
        clear_state()
        
        df = pd.read_csv(file.file)
        datastore.set_dataframe(df, file.filename)
        
        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "rows": len(df),
            "columns": len(df.columns)
        }
    
    except Exception as e:
        raise HTTPException(status_code =400, detail=str(e))