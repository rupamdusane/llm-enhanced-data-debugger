from typing import Dict, List, Any
from app.core.pipeline_state import set_state

def detect_anomalies(inspection_result: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Analyze inspection output and return anomaly signals.
    """
    anomalies = []
    
    row_count = inspection_result.get("rows_count",0)
    columns = inspection_result.get("columns",{})
    
    for col_name, stats in columns.items():
        anomalies.extend(
            analyze_column(col_name, stats, row_count)
        )
    set_state("anomalies", anomalies)
    return anomalies

def analyze_column(
    col_name: str,
    stats: Dict[str, Any],
    row_count: int) -> List[Dict[str, Any]]:
    
    signals = []
    
    nulls = stats.get("null_count", 0)
    dtype = stats.get("dtype")
    samples = stats.get("sample_values", [])
    
    # High null ratio
    if row_count > 0:
        null_ratio = nulls / row_count
        if null_ratio > 0.5:
            signals.append({
                "column": col_name,
                "type": "High_Null_Ratio",
                "severity": "high",
                "details": {"null_ratio": round(null_ratio, 3)}
            })
            
    # Constant column
    unique_samples = set(map(str, samples))
    if len(unique_samples) == 1 and row_count > 1:
        signals.append({
            "column": col_name,
            "type": "CONSTANT_COLUMN",
            "severity": "medium",
            "details": {"value": list(unique_samples)[0]}
        })
        
    # Mixed Type sample detection
    """This cathches:
        - numbers + strings
        - strings + None
        - corrupted CSV columns
    """
    observed_types = set(type(v).__name__ for v in samples if v is not None)

    if len(observed_types) > 1:
        signals.append({
            "column": col_name,
            "type": "MIXED_TYPE_COLUMN",
            "severity": "high",
            "details": {"observed_types": list(observed_types)}
        })
        
    # High cardinality heuristic
    if dtype == "object" and len(unique_samples) >= 10:
        signals.append({
            "column": col_name,
            "type": "HIGH_CARDINALITY_SAMPLE",
            "severity": "low",
            "details": {"unique_sample_count": len(unique_samples)}
        })
        
    return signals