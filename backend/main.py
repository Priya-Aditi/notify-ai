from fastapi import FastAPI
from pydantic import BaseModel

from ai.analyzer import analyze_message
from priority.engine import calculate_priority
from notification.engine import decide_notification

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

    # Step 1: Understand the message
    analysis = analyze_message(request.message)

    # Step 2: Calculate priority
    priority = calculate_priority(analysis)

    # Step 3: Decide notification behavior
    notification = decide_notification(
        priority=priority["priority"],
        category=analysis.category,
        requires_action=analysis.requires_action
    )

    return {
        "analysis": analysis,
        "priority": priority,
        "notification": notification
    }
