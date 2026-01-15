import pandas as pd
from typing import Optional

class DataStore:
    """Central in-memory storage for the upload dataset"""
    
    def __init__(self):
        self.df: Optional[pd.DataFrame] = None
        self.filename: Optional[str] = None

    def set_dataframe(self, df: pd.DataFrame, filename: str):
        self.df = df
        self.filename = filename
        
    def get_dataframe(self) -> pd.DataFrame:
        if self.df is None:
            raise ValueError("No dataset uploaded yet")
        return self.df
    
    def clear(self):
        self.df = None
        self.filename = None
        
# Global singleton instance
datastore = DataStore()

# why a singleton?
# This design allows different parts of the application to access and modify the uploaded dataset without needing to pass around the DataStore instance explicitly.
# - One shared dataset
# - Predictable