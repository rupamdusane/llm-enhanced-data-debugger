from pydnatic import BaseModel
from typing import List, Dict, Any

class ColumnSummary(BaseModel):
    name: str
    data_type: str
    non_null_count: int
    unique_count: int

class InspectResult(BaseModel):
    rows: int
    columns: int
    schema : Dict[str, ColumnSummary]
    Warnings: List[str]