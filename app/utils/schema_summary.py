import pandas as pd

def summarize_dataframe_chunk(df: pd.DataFrame) -> dict:
    """
    Generate column-level statisticals for a single DataFrame chunk.
    """  
    summary = {}

    for col in df.columns:
        series = df[col]
        
        summary[col] = {
            "dtype": str(series.dtype),
            "null_count": int(series.isna().sum()),
            "unique_values": set(series.astype(str).unique()[:100]),
            "sample_values": series.astype(str).head(3).tolist()
        }
    return summary