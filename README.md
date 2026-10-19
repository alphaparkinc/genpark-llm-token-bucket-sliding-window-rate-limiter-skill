# genpark-llm-token-bucket-sliding-window-rate-limiter-skill

[![Verified by Smithery](https://smithery.ai/badge/@alphaparkinc/genpark-llm-token-bucket-sliding-window-rate-limiter-skill)](https://smithery.ai/servers/@alphaparkinc/genpark-llm-token-bucket-sliding-window-rate-limiter-skill)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![Website](https://img.shields.io/badge/Website-GenPark.ai-green)](https://www.genpark.ai)

> Adaptive multi-tier TPM and RPM rate limiter with smooth leaky bucket queuing and predictive burst wait estimation

## Quick Installation & MCP Integration
Add to your Claude Desktop or Cursor configuration:
```json
{
  "mcpServers": {
    "genpark-llm-token-bucket-sliding-window-rate-limiter-skill": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

## Zero Dependencies
Implemented entirely in Python 3 standard library.
