import pytest
from app.ai.services.sentiment import sentiment_analyzer
from app.ai.services.recommendation import recommendation_engine
from app.ai.services.chatbot import chatbot

class TestAIIntegration:
    """Test suite untuk integrasi AI services"""
    
    @pytest.mark.asyncio
    async def test_complete_student_journey(self, sample_student_data):
        """Test: Complete student journey dengan AI"""
        print(f"\n🎯 Testing Complete Student Journey with AI")
        print("=" * 50)
        
        # Step 1: Student chats with bot
        print(f"\n📌 Step 1: Student Chat")
        chat_query = "Saya ingin tahu tentang jurusan komputer"
        chat_result = await chatbot.get_response(chat_query, "student_123")
        print(f"   Query: {chat_query}")
        print(f"   Bot: {chat_result['response'][:100]}...")
        assert chat_result is not None
        
        # Step 2: Analyze student's sentiment
        print(f"\n📌 Step 2: Sentiment Analysis")
        sentiment = await sentiment_analyzer.analyze(chat_query)
        print(f"   Student sentiment: {sentiment.get('sentiment')}")
        print(f"   Confidence: {sentiment.get('confidence')}")
        assert sentiment is not None
        
        # Step 3: Get recommendations
        print(f"\n📌 Step 3: Major Recommendations")
        recommendations = await recommendation_engine.recommend_major(
            sample_student_data
        )
        print(f"   Top recommendation: {recommendations[0]['major_name']}")
        print(f"   Match score: {recommendations[0]['match_score']:.2f}")
        assert len(recommendations) > 0
        
        print("\n✅ All AI services integrated successfully!")