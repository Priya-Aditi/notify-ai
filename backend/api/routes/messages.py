from fastapi import APIRouter, HTTPException

from database.db import (
    get_messages,
    get_unread_messages,
    get_message_by_id,
    mark_message_as_read
)

from schemas.responses import (
    MessagesResponse,
    SingleMessageResponse,
    ReadMessageResponse
)


router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.get(
    "",
    response_model=MessagesResponse
)
def messages():

    return {
        "messages": get_messages()
    }


@router.get(
    "/unread",
    response_model=MessagesResponse
)
def unread_messages():

    return {
        "messages": get_unread_messages()
    }


@router.get(
    "/{message_id}",
    response_model=SingleMessageResponse
)
def get_message(message_id: int):

    message = get_message_by_id(message_id)

    if message is None:
        raise HTTPException(
            status_code=404,
            detail="Message not found"
        )

    return {
        "message": message
    }


@router.patch(
    "/{message_id}/read",
    response_model=ReadMessageResponse
)
def read_message(message_id: int):

    message = get_message_by_id(message_id)

    if message is None:
        raise HTTPException(
            status_code=404,
            detail="Message not found"
        )

    mark_message_as_read(message_id)

    return {
        "message": "Message marked as read",
        "message_id": message_id
    }
