from app.services.llm_client import LLMClient

class MockLLMClient(LLMClient):
    """
    Mock LLM client for testing purposes.
    """
    
    def generate(self, prompt: str) -> str:
        return (
            "LLM analysis (mocked):\n"
            "The detected anomalies indicate potential data quality issues. "
            "Review missing values, inconsistent data types, and high cardinality columns."
            "before downstream analysis."
        )