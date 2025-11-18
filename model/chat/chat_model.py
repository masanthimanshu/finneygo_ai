from pydantic import BaseModel

class ChatInputModel(BaseModel):
    text: str

class ChatOutputModel(BaseModel):
    amount: int
    category: str
    subCategory: str
