from typing import List, Dict, Any

def build_explanation_prompt(
    inspection: Dict[str, Any],
    anomalies: List[Dict[str, Any]]
) -> str:
    """
    Build a structured prompt for LLM explanation.
    """
    
    lines = []
    
    lines.append("You are a data quality expert.")
    lines.append("Explain the following data anomalies clearly and concisely.")
    lines.append("Focus on causes, risks, and suggested fixes.")
    
    lines.append("Dataset summary:")
    lines.append(f"- Total Rows: {inspection.get('rows_count')}")
    lines.append(f"- Total columns: {inspection.get('columns')}")
    
    if not anomalies:
        lines.append("No anomalies detected.")
        return "\n".join(lines)
    
    lines.append("Detected anomalies:")
    
    for idx, anomaly in enumerate(anomalies, start=1):
        lines.append(
            f"{idx}. Column '{anomaly['column']}'- "
            f"Type: {anomaly['type']} - "
            f"Severity: {anomaly['severity']}"
        )
        
        details = anomaly.get("details", {})
        if details:
            lines.append(f"   Details: {details}")
            
    lines.append(
        "\nProvide a short explanation for each anomaly."
        "Do not invent new anomalies."
    )
    
    return "\n".join(lines)