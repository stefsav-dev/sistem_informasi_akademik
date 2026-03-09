import pytest
import asyncio
from typing import Dict, Any
from app.ai.services.sentiment import SentimentAnalyzer
from app.ai.services.recommendation import RecommendationEngine
from app.ai.services.document_verification import DocumentVerifier
from app.ai.services.chatbot import AdmissionsChatbot


@pytest.fixture
def sentiment_service():
    """FIXTURE untuk sentiment analysis service"""
    return SentimentAnalyzer()

@pytest.fixture
def recommendation_service():
    """Fixture untuk recommendation service"""
    return RecommendationEngine()

@pytest.fixture
def document_service():
    """Fixture untuk document verification service"""
    return DocumentVerifier()

@pytest.fixture
def chatbot_service():
    """Fixture untuk sample data"""
    return AdmissionsChatbot()

@pytest.fixture
def sample_student_data() -> Dict[str, Any]:
    """Fixture untuk sample student data"""
    return {
        "name": "Budi Santoso",
        "interests": ["coding", "programming", "komputer"],
        "grades": {
            "matematika": 85,
            "bahasa_indonesia": 80,
            "bahasa_inggris": 75
        },
        "previous_study": "IPA",
        "school": "SMA Negeri 1 Jakarta"
    }

@pytest.fixture
def sample_texts() -> Dict[str, str]:
    """Fixture untuk sample texts"""
    return {
        "positive": "Saya sangat senang dengan pelayanan ini, sangat membantu!",
        "negative": "Saya kecewa sekali, prosesnya lambat dan membingungkan.",
        "neutral": "Saya ingin bertanya tentang jadwal pendaftaran.",
        "mixed": "Pelayanannya baik tapi prosesnya lama."
    }