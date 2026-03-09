from __future__ import annotations

from typing import Any, Dict, List


class AdmissionsChatbot:
    """Rule-based admissions chatbot with simple session memory."""

    def __init__(self) -> None:
        self._sessions: Dict[str, List[str]] = {}

    async def get_response(self, query: str, session_id: str) -> Dict[str, Any]:
        text = (query or "").strip().lower()
        sid = session_id or "default"
        history = self._sessions.setdefault(sid, [])
        history.append(text)

        if any(k in text for k in ["daftar", "pendaftaran", "mendaftar", "syarat"]):
            return {
                "topic": "pendaftaran",
                "confidence": 0.88,
                "response": "Pendaftaran dapat dilakukan online melalui portal SPMB dengan melengkapi data dan dokumen persyaratan.",
            }

        if any(k in text for k in ["biaya", "ukt", "bayar"]):
            return {
                "topic": "biaya",
                "confidence": 0.86,
                "response": "Biaya kuliah bergantung program studi dan jalur masuk. Silakan cek informasi UKT pada halaman resmi kampus.",
            }

        if any(k in text for k in ["beasiswa", "prestasi", "bantuan"]):
            return {
                "topic": "beasiswa",
                "confidence": 0.87,
                "response": "Tersedia beasiswa prestasi dan bantuan ekonomi. Anda bisa menyiapkan dokumen pendukung saat pendaftaran.",
            }

        if any(k in text for k in ["jurusan", "komputer", "informatika"]):
            return {
                "topic": "akademik",
                "confidence": 0.8,
                "response": "Untuk minat komputer, Anda bisa mempertimbangkan Teknik Informatika atau Sistem Informasi.",
            }

        return {
            "topic": "unknown",
            "confidence": 0.45,
            "response": "Maaf, saya belum memahami pertanyaan itu. Coba pertanyaan terkait pendaftaran, biaya, atau beasiswa.",
            "suggestions": ["Cara pendaftaran", "Biaya kuliah", "Informasi beasiswa"],
        }


chatbot = AdmissionsChatbot()
