from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from api.routes.messages import router as messages_router
from services.message_service import process_message
from database.db import initialize_database
from schemas.responses import AnalyzeResponse

# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="NotifyAI",
    description="AI-powered notification prioritization agent",
    version="0.1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Register routers
# --------------------------------------------------

app.include_router(messages_router)


# --------------------------------------------------
# Initialize database
# --------------------------------------------------

initialize_database()


# --------------------------------------------------
# Request model
# --------------------------------------------------

class MessageRequest(BaseModel):
    message: str


# --------------------------------------------------
# Home endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "NotifyAI is running!"
    }


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Analyze message
# --------------------------------------------------

@app.post(
    "/analyze",
    response_model=AnalyzeResponse
)
def analyze(request: MessageRequest):

    return process_message(request.message)
