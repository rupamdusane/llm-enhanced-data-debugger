from app.core.pipeline_state import pipeline_state
from app.schemas.explanation import ExplanationResponse, ExplanationItem
from app.services.prompt_builder import build_explanation_prompt
from app.services.deterministic_explainer import DETERMINISTIC_EXPLANATIONS

def explain_anomalies() -> ExplanationResponse:
    anomalies = pipeline_state.get("anomalies", [])
    inspection = pipeline_state.get("inspection", {})
    
    if not anomalies:
        return ExplanationResponse(
            summary="No anomalies detected. Dataset appears clean.",
            explanations=[]
        )

    explanations: list[ExplanationItem] = []
    
    for anomaly in anomalies:
        explanation_text = (
            DETERMINISTIC_EXPLANATIONS.get(anomaly["type"])
            or generate_mock_explanation(anomaly)
        )
        
        explanations.append(
            ExplanationItem(
                column=anomaly["column"],
                anomaly_type=anomaly["type"],
                severity=anomaly["severity"],
                explanation=explanation_text
            )
        )
        
    # LLM prompt is built but not executed yet
    _ = build_explanation_prompt(inspection, anomalies)
        
    return ExplanationResponse(
        summary=f"{len(explanations)} potential data quality issues detected.",
        explanations=explanations
    )
    
def generate_mock_explanation(anomaly: dict) -> str:
    """
    Mock LLM fallback explanation.
    """
    return (
        f"The column '{anomaly['column']}' shows a "
        f"{anomaly['type']} issue. "
        f"This may impact data quality and downstream analysis."
    )