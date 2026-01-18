from fastapi import HTTPException
from app.core.pipeline_state import get_state

def require_state(key: str):
    if get_state(key) is None:
        raise HTTPException(
            status_code=400,
            detail=f"Pipeline step missing: '{key}' has not been executed."
        )