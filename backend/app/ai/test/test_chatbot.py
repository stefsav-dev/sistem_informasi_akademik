import pytest
from app.ai.services.chatbot import chatbot

class TestChatbot:
    """Test suite untuk Admissions Chatbot"""
    
    @pytest.mark.asyncio
    async def test_pendaftaran_query(self):
        """Test 1: Query tentang pendaftaran"""
        query = "Bagaimana cara mendaftar di kampus ini?"
        session_id = "test_session_1"
        
        print(f"\n💬 Testing query: {query}")
        
        result = await chatbot.get_response(query, session_id)
        
        print(f"   Response: {result.get('response')}")
        print(f"   Topic: {result.get('topic')}")
        print(f"   Confidence: {result.get('confidence')}")
        
        assert result is not None
        assert "response" in result
        assert result["topic"] in ["pendaftaran", "unknown"]
    
    @pytest.mark.asyncio
    async def test_biaya_query(self):
        """Test 2: Query tentang biaya"""
        query = "Berapa biaya kuliah per semester?"
        session_id = "test_session_2"
        
        print(f"\n💬 Testing query: {query}")
        
        result = await chatbot.get_response(query, session_id)
        
        print(f"   Response: {result.get('response')}")
        print(f"   Topic: {result.get('topic')}")
        
        assert result is not None
        assert "response" in result
    
    @pytest.mark.asyncio
    async def test_beasiswa_query(self):
        """Test 3: Query tentang beasiswa"""
        query = "Apakah ada beasiswa untuk siswa berprestasi?"
        session_id = "test_session_3"
        
        print(f"\n💬 Testing query: {query}")
        
        result = await chatbot.get_response(query, session_id)
        
        print(f"   Response: {result.get('response')}")
        print(f"   Topic: {result.get('topic')}")
        
        assert result is not None
    
    @pytest.mark.asyncio
    async def test_conversation_context(self):
        """Test 4: Context dalam percakapan"""
        session_id = "test_session_4"
        
        queries = [
            "Saya ingin mendaftar",
            "Apa saja syaratnya?",
            "Berapa biayanya?"
        ]
        
        print(f"\n💬 Testing conversation context")
        
        for i, query in enumerate(queries, 1):
            result = await chatbot.get_response(query, session_id)
            print(f"\n   Q{i}: {query}")
            print(f"   A: {result.get('response')[:100]}...")
            print(f"   Topic: {result.get('topic')}")
            
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_unknown_query(self):
        """Test 5: Query tidak dikenal"""
        query = "abcdefghijklmnopqrstuvwxyz"
        session_id = "test_session_5"
        
        print(f"\n💬 Testing unknown query")
        
        result = await chatbot.get_response(query, session_id)
        
        print(f"   Response: {result.get('response')}")
        print(f"   Topic: {result.get('topic')}")
        print(f"   Suggestions: {result.get('suggestions')}")
        
        assert result["topic"] == "unknown"
        assert "suggestions" in result