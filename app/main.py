from fastapi import FastAPI
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

app = FastAPI(
    title="Friday AI Assistant",
    version="0.1.0",
    description="Personal AI assistant for Daily tasks and productivity"
)

chat_service = ChatService()

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
@app.post("/chat", response_model=ChatResponse)
def chat(chat_request: ChatRequest):
    return chat_service.get_response(chat_request.message)