from typing import Dict

DETERMINISTIC_EXPLANATIONS: Dict[str, str] = {
    "High_Null_Ratio": (
        "More than half of the values are missing. "
        "This may indicate incomplete data collection or ingestion issues."
    ),
    "CONSTANT_COLUMN": (
        "All sampled values are identical. "
        "This column may not provide useful analytical information."
    ),
    "MIXED_TYPE_COLUMN": (
        "The column contains multiple data types. "
        "This often happens due to parsing errors or inconsistent data entry."
    ),
    "HIGH_CARDINALITY_SAMPLE": (
        "The column has many unique values. "
        "This can affect grouping, joins, and model performance."
    ),
}