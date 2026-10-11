"""MCP server for Cross-Platform Social Scheduler."""
import sys
import json
from client import CrossPlatformSocialScheduler

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "schedule_social_campaign",
                "description": "Adapts announcement into platform-specific posts and optimal UTC time slots",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "core_announcement": {"type": "string"},
                        "target_platforms": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["core_announcement", "target_platforms"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "schedule_social_campaign":
            args = params.get("arguments", {})
            res = CrossPlatformSocialScheduler.synthesize_schedule(
                args.get("core_announcement", ""),
                args.get("target_platforms", [])
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
