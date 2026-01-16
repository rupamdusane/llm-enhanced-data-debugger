class BaseLLMClient:
    """
    Abstract LLM interface.
    Real model will implement this later.
    """
    
    def explain(self, prompt: str) -> str:
        raise NotImplementedError