from os import getenv
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Finneygo", version="1.0.0")

@app.get("/health")
async def health():
    return  {"message": "It's Working", "api_key": getenv("GOOGLE_API_KEY")}

class ChatInputModel(BaseModel):
    text: str

class ChatOutputModel(BaseModel):
    amount: int
    category: str
    subCategory: str

@app.post("/chat", response_model=ChatOutputModel)
async def chat(payload: ChatInputModel):
    return ChatOutputModel(amount=100, category="sample", subCategory="demo")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, reload=True)
