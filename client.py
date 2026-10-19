"""LLM Token Bucket & Sliding Window Rate Limiter.
100% Python Standard Library.
"""
import time

class LLMTokenBucketRateLimiter:
    """Adaptive multi-tier TPM and RPM rate limiter with smooth leaky bucket queuing and predictive burst wait estimation."""

    def __init__(self, max_tpm: int = 40000, max_rpm: int = 60):
        self.max_tpm = max_tpm
        self.max_rpm = max_rpm
        self.tokens_available = float(max_tpm)
        self.last_leak_time = time.time()
        self.request_timestamps = []

    def check_and_reserve(self, estimated_tokens: int) -> dict:
        now = time.time()
        elapsed = now - self.last_leak_time
        replenish_rate = self.max_tpm / 60.0
        self.tokens_available = min(float(self.max_tpm), self.tokens_available + elapsed * replenish_rate)
        self.last_leak_time = now

        self.request_timestamps = [ts for ts in self.request_timestamps if now - ts < 60.0]

        wait_seconds = 0.0
        if len(self.request_timestamps) >= self.max_rpm:
            oldest_ts = self.request_timestamps[0]
            wait_seconds = max(wait_seconds, round(60.0 - (now - oldest_ts) + 0.05, 3))

        if self.tokens_available < estimated_tokens:
            deficit = estimated_tokens - self.tokens_available
            time_to_replenish = deficit / replenish_rate
            wait_seconds = max(wait_seconds, round(time_to_replenish + 0.05, 3))

        allowed = (wait_seconds == 0.0)
        if allowed:
            self.tokens_available -= estimated_tokens
            self.request_timestamps.append(now)

        return {
            "allowed": allowed,
            "wait_seconds": wait_seconds,
            "remaining_tokens": round(self.tokens_available, 1),
            "current_rpm_count": len(self.request_timestamps),
            "max_tpm": self.max_tpm,
            "max_rpm": self.max_rpm
        }
