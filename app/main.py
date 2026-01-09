from app.api.routes import health
from app.api.routes import upload
from app.api.routes import inspect
from app.api.routes import anomalies
from app.api.routes import clean
from fastapi import FastAPI


app = FastAPI(
  title = "LLM Enhanced Data Debugger",
  version = "0.1.0"
)



# Register routers
app.include_router(upload.router, prefix = "/api", tags=["Upload"])
app.include_router(inspect.router, prefix = "/api", tags=["Inspect"])
app.include_router(anomalies.router, prefix = "/api", tags=["Anomalies"])
app.include_router(clean.router, prefix = "/api", tags=["Clean"])
app.include_router(health.router, prefix="/api", tags=["Health"])

