from fastapi import FastAPI
from pydantic import BaseModel

from ai.analyzer import analyze_message
from priority.engine import calculate_priority

from ai.analyzer import analyze_message


app = FastAPI(
    title="NotifyAI",
    description="AI-powered notification prioritization agent",
    version="0.1.0"
)


class MessageRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "NotifyAI is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(request: MessageRequest):

    analysis = analyze_message(request.message)

    priority = calculate_priority(analysis)

    return {
        "analysis": analysis,
        "priority": priority
    }
