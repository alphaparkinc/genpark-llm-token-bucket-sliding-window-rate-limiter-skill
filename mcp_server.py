"""MCP Server wrapper for LLM Token Bucket Rate Limiter."""
import json
import sys
from client import LLMTokenBucketRateLimiter

limiter = LLMTokenBucketRateLimiter()

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "check_llm_rate_limit",
                    "description": "Check and reserve TPM and RPM quotas with predictive sleep duration calculation",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "estimated_tokens": {"type": "integer", "default": 1000}
                        },
                        "required": ["estimated_tokens"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        res = limiter.check_and_reserve(args.get("estimated_tokens", 1000))
        return {
            "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
        }
    return {}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            try:
                r = json.loads(line)
                out = handle_request(r)
                print(json.dumps(out), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)
