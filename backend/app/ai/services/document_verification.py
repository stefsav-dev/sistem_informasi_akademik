from __future__ import annotations

from typing import Any, Dict, List


class DocumentVerifier:
    """Basic document verifier with lightweight byte-content checks."""

    _supported_types = {"ktp", "ijazah"}

    async def verify_document(self, image_bytes: bytes, document_type: str) -> Dict[str, Any]:
        doc_type = (document_type or "").strip().lower()
        result: Dict[str, Any] = {
            "verified": False,
            "confidence": 0.0,
            "document_type": doc_type,
            "issues": [],
            "extracted_data": {},
        }

        if doc_type not in self._supported_types:
            result["issues"].append("Unsupported document type")
            return result

        if not image_bytes:
            result["issues"].append("Empty image input")
            return result

        # Lightweight heuristic: image exists + supported type.
        base_confidence = 0.75
        result["verified"] = True
        result["confidence"] = base_confidence

        # Extracted fields are placeholders for now (real OCR can replace this).
        if doc_type == "ktp":
            result["extracted_data"] = {"document": "KTP", "nik_detected": False}
        elif doc_type == "ijazah":
            result["extracted_data"] = {"document": "Ijazah", "year_detected": False}

        return result


document_verifier = DocumentVerifier()
