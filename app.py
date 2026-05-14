from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from chatbot import generate_response
import os

app = FastAPI(title="Empathy Analyzer API")

class ChatRequest(BaseModel):
    text: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    bot_response = generate_response(request.text)
    return ChatResponse(response=bot_response)

@app.get("/", response_class=HTMLResponse)
async def root():
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Frontend not found. Did you create static/index.html?</h1>"
