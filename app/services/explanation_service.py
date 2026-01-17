from app.core.pipeline_state import pipeline_state
from app.schemas.explanation import ExplanationResponse, ExplanationItem
from app.services.llm.prompt_builder import build_explanaiton_prompt

def explain_anomalies() -> ExplanationResponse:
    anomalies = pipeline_state.get("anomalies", [])
    
    if not anomalies:
        return ExplanationResponse(
            summary="No anomalies detected. Dataset appears clean.",
            explanations=[]
        )

    explanations: list[ExplanationItem] = []
    
    for anomaly in anomalies:
        explanations.append(
            ExplanationItem(
                column=anomaly["column"],
                anomaly_type=anomaly["type"],
                severity=anomaly["severity"],
                explanation=generate_mock_explanation(anomaly)
            )
        )
        
    return ExplanationResponse(
        summary=f"{len(explanations)} potential data quality issues detected.",
        explanations=explanations
    )
    
def generate_mock_explanation(anomaly: dict) -> str:
    """
    Placeholder for real LLM logic.
    """
    return (
        f"The column '{anomaly['column']}' shows a "
        f"{anomaly['type']} issue. "
        f"This may impact data quality and downstream analysis."
    )