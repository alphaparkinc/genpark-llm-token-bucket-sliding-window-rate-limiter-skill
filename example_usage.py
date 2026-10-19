"""Example usage for LLM Token Bucket & Sliding Window Rate Limiter."""
from client import LLMTokenBucketRateLimiter

if __name__ == "__main__":
    limiter = LLMTokenBucketRateLimiter(max_tpm=20000, max_rpm=10)
    res = limiter.check_and_reserve(estimated_tokens=1500)
    print("Rate limit check result:", res)
