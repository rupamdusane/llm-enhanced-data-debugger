from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile
import os

from app.services.inspection_services import inspect_csv_file

router = APIRouter()

@router.post("/inspect")
async def inspect_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    # Temporary file avoids memory overload.
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp_file_path = tmp.name
        tmp.write(await file.read())
        
    try:
        result = inspect_csv_file(tmp_file_path)
        return result
    finally:
        os.remove(tmp_file_path)