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
            "unique_count": int(series.nunique(dropna=True)),
            "sample_values": series.dropna().head(3).tolist()
        }
    return summary