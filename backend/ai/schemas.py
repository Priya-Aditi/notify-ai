from pydantic import BaseModel, Field
from typing import Optional


class MessageAnalysis(BaseModel):
    summary: str

    category: str

    importance: int = Field(
        ge=1,
        le=10
    )

    urgency: int = Field(
        ge=1,
        le=10
    )

    requires_action: bool

    deadline: Optional[str] = None

    suggested_action: Optional[str] = None
