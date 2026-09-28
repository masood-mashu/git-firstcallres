"""
fcr_eligibility_calculator.py - Calculates whether a ticket qualifies as First-Call Resolution based on agent message and reopen count
"""
import sys
import json


def calculate_fcr(ticket_stats_json: str):
    import json
    data = json.loads(ticket_stats_json) if isinstance(ticket_stats_json, str) else ticket_stats_json
    replies = data.get("agent_replies_count", 1)
    reopened = data.get("was_reopened", False)
    is_fcr = replies == 1 and not reopened
    return {
        "agent_replies": replies,
        "reopened": reopened,
        "fcr_achieved": is_fcr,
        "status": "FCR_VERIFIED" if is_fcr else "MULTI_TOUCH_RESOLUTION"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "fcr-eligibility-calculator"}))
