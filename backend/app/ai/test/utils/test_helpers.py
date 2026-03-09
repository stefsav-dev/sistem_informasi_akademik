import time
from typing import Dict, Any
import json

def print_test_result(test_name: str, result: Dict[str, Any], status: str = "PASS"):
    """Print formatted test result"""
    print(f"\n{'-'*50}")
    print(f"📊 Test: {test_name}")
    print(f"   Status: {'✅' if status == 'PASS' else '❌'} {status}")
    print(f"   Time: {time.strftime('%H:%M:%S')}")
    print(f"   Result: {json.dumps(result, indent=2)}")
    print(f"{'-'*50}")

def measure_response_time(func):
    """Decorator to measure response time"""
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()
        print(f"⏱️  Response time: {(end-start)*1000:.2f}ms")
        return result
    return wrapper

def create_test_summary(results: list) -> Dict:
    """Create summary of test results"""
    total = len(results)
    passed = sum(1 for r in results if r.get('status') == 'PASS')
    failed = total - passed
    
    return {
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "success_rate": f"{(passed/total)*100:.1f}%" if total > 0 else "0%",
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }