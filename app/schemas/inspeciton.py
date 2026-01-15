from pydnatic import BaseModel
from typing import List, Dict

class ColumnSummary(BaseModel):
    dtype: str
    null_count: int
    unique_count: int
    sample_values: List

class InspectResult(BaseModel):
    rows_count: int
    columns: int
    schema : Dict[str, ColumnSummary]
    warnings: List[str]