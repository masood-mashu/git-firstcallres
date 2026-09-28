"""
repeat_contact_detector.py - Detects whether customer created a secondary inquiry within 72 hours of ticket closure
"""
import sys
import json


def detect_repeat_contact(hours_since_closure: float, window_hours: float = 72.0):
    is_repeat = hours_since_closure <= window_hours
    return {
        "hours_since_last_ticket": hours_since_closure,
        "threshold_window": window_hours,
        "repeat_contact": is_repeat,
        "status": "REPEAT_CONTACT_DETECTED" if is_repeat else "NEW_INDEPENDENT_CONTACT"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "repeat-contact-detector"}))
