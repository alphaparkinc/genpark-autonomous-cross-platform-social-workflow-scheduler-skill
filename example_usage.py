"""Example usage for Cross-Platform Social Scheduler."""
from client import CrossPlatformSocialScheduler

if __name__ == "__main__":
    res = CrossPlatformSocialScheduler.synthesize_schedule(
        "Shipping our new zero-dependency MCP agent runtime!",
        ["x_twitter", "linkedin", "instagram"]
    )
    print("Campaign Status:", res["campaign_status"])
    for p in res["posts"]:
        print(f"[{p['platform']}] ({p['recommended_slot_utc']}): {p['adapted_copy'][:60]}...")
