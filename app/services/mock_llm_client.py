from app.services.llm_client import LLMClient

class MockLLMClient(LLMClient):
    """
    Mock LLM client for testing purposes.
    """
    
    def generate(self, prompt: str) -> str:
        return (
            "LLM analysis (mocked):\n"
            "Based on the dataset inspection, this anomaly indicates a potential "
            "data quality issue that may affect downstream analytics. "
            "Recommended action: review source data and apply validation rules."
        )