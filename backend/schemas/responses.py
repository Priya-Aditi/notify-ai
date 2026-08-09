from pydantic import BaseModel
from typing import Optional


class PriorityResponse(BaseModel):
    priority: str
    label: str
    score: float
    reason: str


class NotificationResponse(BaseModel):
    action: str
    reason: str


class ActionResponse(BaseModel):
    executed: bool
    action: str
    message: str


class AnalysisResponse(BaseModel):
    summary: str
    category: str
    importance: int
    urgency: int
    requires_action: bool
    deadline: Optional[str] = None
    suggested_action: Optional[str] = None


class AnalyzeResponse(BaseModel):
    message_id: int
    analysis: AnalysisResponse
    priority: PriorityResponse
    notification: NotificationResponse
    action: ActionResponse


class MessageResponse(BaseModel):
    id: int
    message: str
    summary: Optional[str] = None
    category: Optional[str] = None
    importance: Optional[int] = None
    urgency: Optional[int] = None
    requires_action: bool
    deadline: Optional[str] = None
    suggested_action: Optional[str] = None
    priority: Optional[str] = None
    priority_label: Optional[str] = None
    priority_score: Optional[float] = None
    notification_action: Optional[str] = None
    notification_reason: Optional[str] = None
    is_read: bool
    created_at: str


class MessagesResponse(BaseModel):
    messages: list[MessageResponse]


class SingleMessageResponse(BaseModel):
    message: MessageResponse


class ReadMessageResponse(BaseModel):
    message: str
    message_id: int
