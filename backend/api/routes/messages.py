from fastapi import APIRouter

from database.db import (
    get_messages,
    get_unread_messages,
    get_message_by_id,
    mark_message_as_read
)


router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.get("")
def messages():

    return {
        "messages": get_messages()
    }


@router.get("/unread")
def unread_messages():

    return {
        "messages": get_unread_messages()
    }


@router.get("/{message_id}")
def get_message(message_id: int):

    message = get_message_by_id(message_id)

    if message is None:
        return {
            "error": "Message not found"
        }

    return {
        "message": message
    }


@router.patch("/{message_id}/read")
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
