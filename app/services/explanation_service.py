from app.core.pipeline_state import get_state
from app.schemas.explanation import ExplanationResponse, ExplanationItem
from app.services.llm.prompt_builder import build_explanaiton_prompt

def explain_anomalies() -> ExplanationResponse:
    anomalies = get_state("anomalies")
    
    if not anomalies:
        return ExplanationResponse(
            summary="No anomalies detected.",
            explanations=[]
        )

    # Mock explanations (No real LLM integration yet)
    explanations = []
    
    for a in anomalies:
        explanations.append(
            ExplanationItem(
                anomaly_type=a.get("type", "unknown"),
                column=a.get("column", "unknown"),
                explanation=f"The column '{a.get('column')}' has an issue of type '{a.get('type')}'."
            )
        )
        
    return ExplanationResponse(
        summary=f"{len(explanations)} data quality issues detected.",
        explanations=explanations
    )