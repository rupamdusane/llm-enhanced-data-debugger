"""
Orchestrates CSV inspection:
- chunk reading
- schema inference
- statistics collection
"""
    
import pandas as pd
from app.utils.schema_summary import summarize_dataframe_chunk

def inspect_dataframe(df: pd.DataFrame) -> dict:
    aggregated_schema = {}
    warnings = []
    
    try:
        total_rows = len(df)
        chunk_summary = summarize_dataframe_chunk(df)
            
        for col, stats in chunk_summary.items():
            aggregated_schema[col] = {
                "dtype": stats["dtype"],
                "null_count": stats["null_count"],
                "unique_count": len(stats["unique_values"]),
                "sample_values": stats['sample_values']
            }
                 
    except Exception as e:
        warnings.append(str(e))

    return {
        "rows_count": total_rows,
        "columns": len(aggregated_schema),
        "schema": aggregated_schema,
        "warnings": warnings
    }