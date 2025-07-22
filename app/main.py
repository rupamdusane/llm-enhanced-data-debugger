from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title = "LLM Enhanced Data Debugger")

app.include_router(router)

@app.get("/")
async def root():
    return {"message" : "LLM Data Debugger backend is running!"}