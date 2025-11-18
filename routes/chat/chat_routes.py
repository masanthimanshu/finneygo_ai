from fastapi import APIRouter
from model import ChatInputModel, ChatOutputModel

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/chat", response_model=ChatOutputModel)
async def chat(payload: ChatInputModel) -> ChatOutputModel:
    return ChatOutputModel(amount=100, category="sample", subCategory="demo")
