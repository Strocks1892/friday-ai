from fastapi import FastAPI

app = FastAPI(
    title="Friday AI Assistant",
    version="0.1.0",
    description="Personal AI assistant for Daily tasks and productivity"
)

@app.get("/")
def home():
    return{
        "message": "Welcome to Friday AI Assistant!!",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return{
        "status": "healthy"
    }