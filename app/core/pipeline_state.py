"""
    Central in-memory pipeline state.
    Used to share data between inspection, anomalies, and explanation stages.
"""
    
pipeline_state: dict = {}

def set_state(key: str, value):
    pipeline_state[key] = value
    
def get_state(key: str, default=None):
    return pipeline_state.get(key, default)

def clear_state():
    pipeline_state.clear()