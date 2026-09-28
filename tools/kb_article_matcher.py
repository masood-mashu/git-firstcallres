"""
kb_article_matcher.py - Checks if an incoming ticket issue category has an active, verified knowledge base article
"""
import sys
import json


def match_kb_article(issue_category: str):
    PUBLISHED_KB = ["password reset", "invoice download", "2fa setup", "api keys", "upgrade plan"]
    norm = issue_category.strip().lower()
    has_article = any(k in norm for k in PUBLISHED_KB)
    return {
        "category": issue_category,
        "kb_article_exists": has_article,
        "action_required": "NONE" if has_article else "DRAFT_NEW_KB_ARTICLE",
        "status": "KB_DOCUMENTED" if has_article else "KB_GAP_DETECTED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "kb-article-matcher"}))
