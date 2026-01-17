from typing import Optional

class LLMClient:
    """
    Base LLM interface.
    """
    
    def generate(self, prompt: str) -> Optional[str]:
        raise NotImplementedError