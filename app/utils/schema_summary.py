import pandas as pd
from io import BytesIO

def generate_schema_summary(file_bytes: bytes):
    df = pd.read_csv(BytesIO(file_bytes))
    
    summary = {
        "columns": list(df.columns),
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "sample_rows": df.head(5).to_dict(orient="records")


    }
    
    return summary