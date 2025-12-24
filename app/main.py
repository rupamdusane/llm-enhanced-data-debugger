from fastapi import FastAPI
from app.api.routes.upload import router as upload_router
from app.api.routes.inspect import router as inspect_router
from app.api.routes.anomalies import router as anomalies_router
from app.api.routes.clean import router as clean_router

app = FastAPI(
  title = "LLM Enhanced Data Debugger",
  version = "0.1.0"
)

@app.get("/")
def home():
  return {"message": "Backend is running"}

# Register routers
app.include_router(upload_router, prefix = "/api/upload", tags=["Upload"])
app.include_router(inspect_router, prefix = "/api/inspect", tags=["Inspect"])
app.include_router(anomalies_router, prefix = "/api/anomalies", tags=["Anomalies"])
app.include_router(clean_router, prefix = "/api/clean", tags=["Clean"])

