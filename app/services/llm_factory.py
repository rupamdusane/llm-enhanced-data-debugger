import os
from app.services.mock_llm_client import MockLLMClient
from app.services.llm_client import LLMClient

def get_llm_client() -> LLMClient:
    """
    Return configured LLM client.
    Default: MockLLMClient for testing.
    """
    
    provider = os.getenv("LLM_PROVIDER", "mock")
    
    if provider == "mock":
        return MockLLMClient()
    
    #Future: Real LLM
    return MockLLMClient()