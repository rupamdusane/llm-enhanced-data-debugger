from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    # To support different file formats
    filename = file.filename.lower()
    
    content = await file.read()
    
    # CSV
    if filename.endswitch(".csv"):
        df = pd.read_csv(BytesIO(content))
        
    # xlsx
    elif filename.endswitch(".xlsx"):
        df = pd.read_excel(BytesIO(content))
        
    # JSON
    elif filename.endswitch(".json"):
        df = pd.read_json(BytesIO(content))
        
    
    else:
        raise HTTPExecution(
            status_code=400,
            detail = "Only CSV, XLSX and JSON files are supported"
        )
        
    return{
        "filename": file.filename,
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict()
    }