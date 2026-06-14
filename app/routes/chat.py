from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.groq_service import get_chat_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = get_chat_response(request.message, request.history)
    return ChatResponse(response=response)