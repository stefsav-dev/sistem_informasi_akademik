from __future__ import annotations

from typing import Dict, List


class SentimentAnalyzer:
    """Simple rule-based sentiment analyzer for Indonesian text."""

    _positive_keywords = {
        "senang",
        "bagus",
        "baik",
        "membantu",
        "suka",
        "puas",
        "cepat",
    }
    _negative_keywords = {
        "kecewa",
        "buruk",
        "lambat",
        "bingung",
        "marah",
        "sulit",
        "jelek",
    }

    async def analyze(self, text: str) -> Dict[str, float | str]:
        cleaned = (text or "").strip().lower()
        if not cleaned:
            return {"sentiment": "neutral", "confidence": 0.5}

        pos_hits = sum(1 for k in self._positive_keywords if k in cleaned)
        neg_hits = sum(1 for k in self._negative_keywords if k in cleaned)

        if pos_hits > neg_hits:
            score = min(0.99, 0.6 + 0.1 * (pos_hits - neg_hits))
            return {"sentiment": "positive", "confidence": round(score, 2)}
        if neg_hits > pos_hits:
            score = min(0.99, 0.6 + 0.1 * (neg_hits - pos_hits))
            return {"sentiment": "negative", "confidence": round(score, 2)}

        return {"sentiment": "neutral", "confidence": 0.55}

    async def analyze_batch(self, texts: List[str]) -> List[Dict[str, float | str]]:
        return [await self.analyze(text) for text in texts]


sentiment_analyzer = SentimentAnalyzer()
