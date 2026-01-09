from fastapi import APIRouter, UploadFile, File

router = APIRouter()
@router.post("/inspect")
async def inspect_file(file: UploadFile = File(...)):
    """
    Accepts a CSV file and returns schema + metadata summary.
    """
    return{
        "filename": file.filename,
        "status": "Inspect endpoint placeholder"
    }