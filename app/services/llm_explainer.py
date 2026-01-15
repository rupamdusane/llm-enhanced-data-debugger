from typing import Dict, List

def explain_anomalies(anomalies: List[Dict], llm_client) -> List[Dict]:
    explanations = []

    for anomaly in anomalies:
        prompt = build_prompt(anomaly)
        response = llm_client(prompt)

        explanations.append({
            "column": anomaly["column"],
            "anomaly_type": anomaly["type"],
            "llm_explanation": response
        })

    return explanations

def build_prompt(anomaly: Dict) -> str:
    return f"""
You are a data quality expert.str

Column: {anomaly['column']}
Anomaly Type: {anomaly['type']}
Metrics: {anomaly['metrics']}

Expalin:
1. What the issue is
2. Why it matters
3. What should be done
"""