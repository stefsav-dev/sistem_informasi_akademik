from __future__ import annotations

from typing import Any, Dict, List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RecommendationEngine:
    """Recommendation engine using scikit-learn TF-IDF similarity."""

    _majors = [
        {
            "major_name": "Teknik Informatika",
            "description": "Fokus pada pemrograman, sistem, dan rekayasa perangkat lunak.",
            "keywords": {"komputer", "coding", "programming", "teknologi"},
        },
        {
            "major_name": "Sistem Informasi",
            "description": "Menggabungkan bisnis, manajemen, dan teknologi informasi.",
            "keywords": {"bisnis", "manajemen", "data", "komputer"},
        },
        {
            "major_name": "Manajemen",
            "description": "Mempelajari pengelolaan organisasi dan strategi bisnis.",
            "keywords": {"bisnis", "ekonomi", "organisasi", "manajemen"},
        },
        {
            "major_name": "Ilmu Komunikasi",
            "description": "Fokus pada komunikasi, media, dan strategi publik.",
            "keywords": {"komunikasi", "media", "public speaking", "konten"},
        },
    ]

    def __init__(self) -> None:
        # Build corpus once so inference remains lightweight.
        self._vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        major_docs = [self._major_document(major) for major in self._majors]
        self._major_matrix = self._vectorizer.fit_transform(major_docs)

    def _major_document(self, major: Dict[str, Any]) -> str:
        keywords = " ".join(sorted(major["keywords"]))
        return f"{major['major_name']} {major['description']} {keywords}".lower()

    def _student_document(self, student_data: Dict[str, Any]) -> str:
        interests = student_data.get("interests", []) or []
        interests_text = " ".join(str(item).strip().lower() for item in interests if str(item).strip())
        background = str(student_data.get("previous_study", "")).lower()
        return f"{interests_text} {background}".strip()

    async def recommend_major(
        self, student_data: Dict[str, Any], n_recommendations: int = 3
    ) -> List[Dict[str, Any]]:
        student_doc = self._student_document(student_data)
        if not student_doc:
            student_doc = "umum pendidikan"

        student_vector = self._vectorizer.transform([student_doc])
        similarity_scores = cosine_similarity(student_vector, self._major_matrix)[0]

        grades = student_data.get("grades", {}) or {}
        avg_grade = sum(grades.values()) / max(1, len(grades))
        grade_score = max(0.0, min(1.0, avg_grade / 100))

        scored: List[Dict[str, Any]] = []
        for idx, major in enumerate(self._majors):
            text_score = float(similarity_scores[idx])  # 0..1
            match_score = 0.7 * text_score + 0.3 * grade_score

            scored.append(
                {
                    "major_name": major["major_name"],
                    "description": major["description"],
                    "match_score": round(match_score, 2),
                }
            )

        scored.sort(key=lambda x: x["match_score"], reverse=True)
        return scored[: max(1, n_recommendations)]


recommendation_engine = RecommendationEngine()
