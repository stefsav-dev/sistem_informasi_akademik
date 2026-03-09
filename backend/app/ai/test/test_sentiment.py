import pytest
from app.ai.services.sentiment import sentiment_analyzer
import asyncio

class TestSentimentAnalyzer:
    """Test suite untuk Sentiment Analyzer"""
    
    @pytest.mark.asyncio
    async def test_sentiment_positive(self, sample_texts):
        """Test 1: Analisis sentimen positif"""
        text = sample_texts["positive"]
        print(f"\n📝 Testing positive sentiment: {text}")
        
        result = await sentiment_analyzer.analyze(text)
        
        print(f"   Hasil: {result}")
        
        assert result is not None
        assert "sentiment" in result
        assert "confidence" in result
        assert result["confidence"] > 0
        assert result["sentiment"] in ["positive", "POSITIVE", "LABEL_1"]
    
    @pytest.mark.asyncio
    async def test_sentiment_negative(self, sample_texts):
        """Test 2: Analisis sentimen negatif"""
        text = sample_texts["negative"]
        print(f"\n📝 Testing negative sentiment: {text}")
        
        result = await sentiment_analyzer.analyze(text)
        
        print(f"   Hasil: {result}")
        
        assert result is not None
        assert "sentiment" in result
        assert result["confidence"] > 0
    
    @pytest.mark.asyncio
    async def test_sentiment_neutral(self, sample_texts):
        """Test 3: Analisis sentimen netral"""
        text = sample_texts["neutral"]
        print(f"\n📝 Testing neutral sentiment: {text}")
        
        result = await sentiment_analyzer.analyze(text)
        
        print(f"   Hasil: {result}")
        assert result is not None
    
    @pytest.mark.asyncio
    async def test_empty_text(self):
        """Test 4: Text kosong"""
        text = ""
        print(f"\n📝 Testing empty text")
        
        result = await sentiment_analyzer.analyze(text)
        
        print(f"   Hasil: {result}")
        # Should handle gracefully
        assert result is not None
    
    @pytest.mark.asyncio
    async def test_long_text(self):
        """Test 5: Text panjang"""
        text = "Ini adalah text yang sangat panjang. " * 100
        print(f"\n📝 Testing long text ({len(text)} characters)")
        
        result = await sentiment_analyzer.analyze(text)
        
        print(f"   Hasil: {result}")
        assert result is not None
    
    @pytest.mark.asyncio
    async def test_batch_analysis(self, sample_texts):
        """Test 6: Batch analysis multiple texts"""
        texts = list(sample_texts.values())
        print(f"\n📝 Testing batch analysis with {len(texts)} texts")
        
        results = await sentiment_analyzer.analyze_batch(texts)
        
        print(f"   Hasil: {results}")
        assert len(results) == len(texts)
        for result in results:
            assert "sentiment" in result