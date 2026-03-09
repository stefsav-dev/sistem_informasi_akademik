from __future__ import annotations

from typing import Any, Dict, List


class RecommendationEngine:
    """Simple recommendation engine based on interests and grades."""

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

    async def recommend_major(
        self, student_data: Dict[str, Any], n_recommendations: int = 3
    ) -> List[Dict[str, Any]]:
        interests = {
            str(item).strip().lower()
            for item in student_data.get("interests", [])
            if str(item).strip()
        }
        grades = student_data.get("grades", {}) or {}
        avg_grade = sum(grades.values()) / max(1, len(grades))
        grade_score = max(0.0, min(1.0, avg_grade / 100))

        scored: List[Dict[str, Any]] = []
        for major in self._majors:
            interest_hits = len(interests.intersection(major["keywords"]))
            interest_score = interest_hits / max(1, len(major["keywords"]))
            match_score = 0.65 * interest_score + 0.35 * grade_score

            # Small baseline so empty interests still produce recommendations.
            if not interests:
                match_score = max(match_score, 0.3 + 0.4 * grade_score)

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
