from typing import List

from app.core.pipeline_state import get_state
from app.schemas.explanation import ExplanationResponse, ExplanationItem
from app.services.prompt_builder import build_explanation_prompt
from app.services.deterministic_explainer import DETERMINISTIC_EXPLANATIONS
from app.services.mock_llm_client import MockLLMClient

# Initialize mock LLM client
llm_client = MockLLMClient()

def explain_anomalies() -> ExplanationResponse:
    anomalies = get_state("anomalies", [])
    inspection = get_state("inspection", {})
    
    if not anomalies:
        return ExplanationResponse(
            summary="No anomalies detected. Dataset appears clean.",
            explanations=[]
        )

    explanations: list[ExplanationItem] = []
    
    for anomaly in anomalies:
        # Deterministic explanation first
        explanation_text = DETERMINISTIC_EXPLANATIONS.get(anomaly["type"])
        
        # LLM fallback if no deterministic explanation found
        if explanation_text is None:
            try:
                prompt = build_explanation_prompt(inspection, [anomaly])
                explanation_text = llm_client.generate(prompt)
            except Exception:
                explanation_text = generate_mock_explanation(anomaly)
        
        explanations.append(
            ExplanationItem(
                column=anomaly["column"],
                anomaly_type=anomaly["type"],
                severity=anomaly["severity"],
                explanation=explanation_text
            )
        )
        
    return ExplanationResponse(
        summary=f"{len(explanations)} potential data quality issues detected.",
        explanations=explanations
    )
    
def generate_mock_explanation(anomaly: dict) -> str:
    """
    Final safety fallback explanation.
    """
    return (
        f"The column '{anomaly['column']}' shows a "
        f"{anomaly['type']} issue. "
        f"This may impact data quality and downstream analysis."
    )