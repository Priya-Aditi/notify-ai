from fastapi import FastAPI
from pydantic import BaseModel

from ai.analyzer import analyze_message
from priority.engine import calculate_priority
from notification.engine import decide_notification
from actions.executor import execute_action
from database.db import initialize_database, save_message

from ai.analyzer import analyze_message

from database.db import (
    initialize_database,
    save_message,
    get_messages,
    get_unread_messages,
    get_message_by_id,
    mark_message_as_read
)

app = FastAPI(
    title="NotifyAI",
    description="AI-powered notification prioritization agent",
    version="0.1.0"
)

initialize_database()


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

    # Step 4: Save the message
    message_id = save_message(
        message=request.message,
        summary=analysis.summary,
        category=analysis.category,
        importance=analysis.importance,
        urgency=analysis.urgency,
        requires_action=analysis.requires_action,
        deadline=analysis.deadline,
        suggested_action=analysis.suggested_action,
        priority=priority["priority"],
        priority_label=priority["label"],
        priority_score=priority["score"],
        notification_action=notification["action"],
        notification_reason=notification["reason"]
    )

    # Step 5: Execute notification decision
    action_result = execute_action(
        action=notification["action"],
        message=request.message,
        priority=priority["priority"]
    )

    return {
        "message_id": message_id,
        "analysis": analysis,
        "priority": priority,
        "notification": notification,
        "action": action_result
    }


@app.get("/messages")
def messages():

    return {
        "messages": get_messages()
    }


@app.get("/messages/unread")
def unread_messages():

    return {
        "messages": get_unread_messages()
    }


@app.get("/messages/{message_id}")
def get_message(message_id: int):

    message = get_message_by_id(message_id)

    if message is None:
        return {
            "error": "Message not found"
        }

    return {
        "message": message
    }


@app.patch("/messages/{message_id}/read")
def read_message(message_id: int):

    message = get_message_by_id(message_id)

    if message is None:
        return {
            "error": "Message not found"
        }

    mark_message_as_read(message_id)

    return {
        "message": "Message marked as read",
        "message_id": message_id
    }
