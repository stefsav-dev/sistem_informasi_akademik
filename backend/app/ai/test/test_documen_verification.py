import pytest
import io
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from app.ai.services.document_verification import document_verifier

class TestDocumentVerification:
    """Test suite untuk Document Verification"""
    
    def create_test_image(self, text: str, size=(800, 500)):
        """Helper: Buat image test dengan text"""
        image = Image.new('RGB', size, color='white')
        draw = ImageDraw.Draw(image)
        draw.text((50, 50), text, fill='black')
        return image
    
    @pytest.mark.asyncio
    async def test_verify_ktp(self):
        """Test 1: Verifikasi KTP"""
        # Buat dummy KTP
        ktp_text = """
        PROVINSI DKI JAKARTA
        KABUPATEN ADMINISTRASI JAKARTA SELATAN
        NIK: 3174051234567890
        Nama: BUDI SANTOSO
        Tempat/Tgl Lahir: Jakarta, 12-05-1990
        """
        
        image = self.create_test_image(ktp_text)
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        print(f"\n📄 Testing KTP verification")
        
        result = await document_verifier.verify_document(img_bytes, "ktp")
        
        print(f"   Verified: {result.get('verified')}")
        print(f"   Confidence: {result.get('confidence')}")
        print(f"   Extracted: {result.get('extracted_data', {})}")
        
        assert result is not None
        assert "verified" in result
        assert "confidence" in result
    
    @pytest.mark.asyncio
    async def test_verify_ijazah(self):
        """Test 2: Verifikasi Ijazah"""
        ijazah_text = """
        IJAZAH
        SEKOLAH MENENGAH ATAS
        Nama: SITI AISYAH
        Tempat/Tgl Lahir: Bandung, 15 Agustus 2005
        Tahun Lulus: 2023
        """
        
        image = self.create_test_image(ijazah_text)
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        print(f"\n📄 Testing Ijazah verification")
        
        result = await document_verifier.verify_document(img_bytes, "ijazah")
        
        print(f"   Verified: {result.get('verified')}")
        print(f"   Issues: {result.get('issues', [])}")
        
        assert result is not None
    
    @pytest.mark.asyncio
    async def test_invalid_document_type(self):
        """Test 3: Tipe dokumen tidak valid"""
        image = self.create_test_image("Test")
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        print(f"\n📄 Testing invalid document type")
        
        result = await document_verifier.verify_document(img_bytes, "invalid_type")
        
        print(f"   Result: {result}")
        
        assert "verified" in result
    
    @pytest.mark.asyncio
    async def test_empty_image(self):
        """Test 4: Image kosong"""
        print(f"\n📄 Testing empty image")
        
        result = await document_verifier.verify_document(b"", "ktp")
        
        print(f"   Result: {result}")
        assert result is not None