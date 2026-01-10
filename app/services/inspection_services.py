
"""
Orchestrates CSV inspection:
- chunk reading
- schema inference
- statistics collection
"""
    
import pandas as pd
from app.utils.schema_summary import summarize_dataframe_chunk

def inspect_csv_file(file_path: str, chunksize: int = 100_000) -> dict:
    total_rows = 0
    bad_lines = 0
    aggregated_schema = {}
    warnings = []
    
    try:
        reader = pd.read_csv(file_path, chunksize=chunksize, on_bad_lines='skip')
        
        for chunk in reader:
            total_rows += len(chunk)
            
            chunk_summary = summarize_dataframe_chunk(chunk)
            
            for col, stats in chunk_summary.items():
                if col not in aggregated_schema:
                    aggregated_schema[col] = {
                        "dtype": stats["dtype"],
                        "null_count": 0,
                        "unique_count": set(),
                        "sample_values": stats['sample_values']
                    }
                    
                aggregated_schema[col]["null_count"] += stats["null_count"]
                aggregated_schema[col]["unique_count"].update(stats["sample_values"])
                
    except Exception as e:
        warnings.append(str(e))
        
    final_schema = {}
    for col, stats in aggregated_schema.items():
        final_schema[col] = {
            "dtype": stats["dtype"],
            "null_count": stats["null_count"],
            "unique_count": len(stats["unique_count"]),
            "sample_values": list(stats["sample_values"])
        }
        
    return {
        "rows": total_rows,
        "columns": len(final_schema),
        "schema": final_schema,
        "warnings": warnings
    }