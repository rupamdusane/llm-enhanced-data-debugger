from typing import Dict, List, Any

def explain_anomalies(anomalies: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Convert detected anomalies into human-readable explanations.
    """
    
    if not anomalies:
        return {
            "summary": "No anomalies detected. Dataset appears clean.",
            "explanations": []
        }
        
    explanations = []
        
    for anomaly in anomalies:
        explanation_text = generate_explanation(anomaly)
        explanations.append({
           "anomaly_type": anomaly["type"],
           "column": anomaly["column"],
           "explanation": explanation_text
        })
            
    summary = f"{len(anomalies)} potential data quality issues detected."
        
    return {
        "summary": summary,
        "explanations": explanations
    }
    
def generate_explanation(anomaly: Dict[str, Any]) -> str:
    """
    Deterministic explanation generator.
    """
    anomaly_type = anomaly["type"]
    column = anomaly["column"]
    details = anomaly.get("details", {})
    
    if anomaly_type == "High_Null_Ratio":
        ratio = details.get("null_ratio", "unknown")
        return (
            f"Column '{column}' contains a high proportion of missing values "
            f"({ratio * 100 if isinstance(ratio, float) else ratio}%). "
            "This may reduce data reliability or model performance."
        )
        
    if anomaly_type == "CONSTANT_COLUMN":
        value = details.get("value", "unknown")
        return (
            f"Column '{column}' has the same value '{value}' for all rows."
            "This column may not be useful for analysis."
        )
        
    if anomaly_type == "MIXED_TYPE_COLUMN":
        observed = ", ".join(details.get("observed_types", []))
        return (
            f"Column '{column}' contains mixed data types: {observed}. "
            "This may indicate data corruption or inconsistent formatting."
        )
        
    if anomaly_type == "HIGH_CARDINALITY_SAMPLE":
        count = details.get("unique_sample_count", "many")
        return (
            f"Column '{column}' has high cardinality (sample size: {count}). "
            "This may impact memory usage and model generalization."
        )
        
    return (
        f"Column '{column}' has an anomaly of type '{anomaly_type}'. "
        "Further investigation is recommended."
    )