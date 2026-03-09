from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, Field

from app.ai.services.chatbot import chatbot
from app.ai.services.document_verification import document_verifier
from app.ai.services.recommendation import recommendation_engine
from app.ai.services.sentiment import sentiment_analyzer

router = APIRouter(prefix="/ai", tags=["AI"])


class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1)


class SentimentBatchRequest(BaseModel):
    texts: List[str] = Field(..., min_length=1)


class RecommendationRequest(BaseModel):
    name: Optional[str] = None
    interests: List[str] = Field(default_factory=list)
    grades: Dict[str, float] = Field(default_factory=dict)
    previous_study: Optional[str] = None
    school: Optional[str] = None


class ChatbotRequest(BaseModel):
    query: str = Field(..., min_length=1)
    session_id: str = Field(..., min_length=1)


@router.get("/health")
async def ai_health() -> Dict[str, str]:
    return {"status": "ok", "service": "ai"}


@router.post("/sentiment")
async def analyze_sentiment(payload: SentimentRequest) -> Dict[str, Any]:
    return await sentiment_analyzer.analyze(payload.text)


@router.post("/sentiment/batch")
async def analyze_sentiment_batch(payload: SentimentBatchRequest) -> List[Dict[str, Any]]:
    return await sentiment_analyzer.analyze_batch(payload.texts)


@router.post("/recommendation/major")
async def recommend_major(payload: RecommendationRequest) -> List[Dict[str, Any]]:
    return await recommendation_engine.recommend_major(payload.model_dump())


@router.post("/chatbot")
async def chatbot_response(payload: ChatbotRequest) -> Dict[str, Any]:
    return await chatbot.get_response(payload.query, payload.session_id)


@router.post("/verify-document")
async def verify_document(
    file: UploadFile = File(...),
    document_type: str = Form(...),
) -> Dict[str, Any]:
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")
    return await document_verifier.verify_document(content, document_type)
