import pytest
from app.ai.services.recommendation import recommendation_engine

class TestRecommendationEngine:
    """Test suite untuk Recommendation Engine"""
    
    @pytest.mark.asyncio
    async def test_recommend_with_interests(self, sample_student_data):
        """Test 1: Rekomendasi berdasarkan minat"""
        print(f"\n📊 Testing recommendation with interests")
        print(f"   Student: {sample_student_data['name']}")
        print(f"   Interests: {sample_student_data['interests']}")
        
        result = await recommendation_engine.recommend_major(
            sample_student_data,
            n_recommendations=3
        )
        
        print(f"\n   Rekomendasi:")
        for i, rec in enumerate(result, 1):
            print(f"   {i}. {rec['major_name']} - Match: {rec['match_score']:.2f}")
            print(f"      {rec['description']}")
        
        assert len(result) <= 3
        assert all("major_name" in r for r in result)
        assert all("match_score" in r for r in result)
    
    @pytest.mark.asyncio
    async def test_recommend_without_interests(self):
        """Test 2: Rekomendasi tanpa data minat"""
        student_data = {
            "name": "Test Student",
            "interests": [],
            "grades": {"matematika": 80},
            "previous_study": "IPA"
        }
        
        print(f"\n📊 Testing recommendation without interests")
        
        result = await recommendation_engine.recommend_major(student_data)
        
        print(f"   Hasil: {len(result)} rekomendasi")
        assert len(result) > 0
    
    @pytest.mark.asyncio
    async def test_recommend_different_grades(self):
        """Test 3: Pengaruh nilai terhadap rekomendasi"""
        student_high = {
            "name": "Student A",
            "interests": ["komputer"],
            "grades": {"matematika": 95},
            "previous_study": "IPA"
        }
        
        student_low = {
            "name": "Student B",
            "interests": ["komputer"],
            "grades": {"matematika": 60},
            "previous_study": "IPA"
        }
        
        print(f"\n📊 Testing grade impact on recommendations")
        
        result_high = await recommendation_engine.recommend_major(student_high)
        result_low = await recommendation_engine.recommend_major(student_low)
        
        # Student dengan nilai tinggi harusnya dapat score lebih tinggi
        print(f"   High grade student top score: {result_high[0]['match_score']:.2f}")
        print(f"   Low grade student top score: {result_low[0]['match_score']:.2f}")
        
        assert result_high[0]['match_score'] >= result_low[0]['match_score']
    
    @pytest.mark.asyncio
    async def test_different_study_backgrounds(self):
        """Test 4: Pengaruh latar belakang studi"""
        students = [
            {
                "name": "IPA Student",
                "interests": ["komputer"],
                "previous_study": "IPA",
                "grades": {"matematika": 80}
            },
            {
                "name": "IPS Student",
                "interests": ["bisnis"],
                "previous_study": "IPS",
                "grades": {"matematika": 75}
            }
        ]
        
        print(f"\n📊 Testing different study backgrounds")
        
        for student in students:
            result = await recommendation_engine.recommend_major(student)
            print(f"\n   {student['name']}:")
            print(f"   Top recommendation: {result[0]['major_name']}")
            print(f"   Score: {result[0]['match_score']:.2f}")