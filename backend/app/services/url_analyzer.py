"""URL structural risk scoring — Member 4's module."""
import re
from urllib.parse import urlparse

SHORTENERS = ["bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly", "is.gd", "buff.ly"]
SUSPICIOUS_WORDS = [
    "verify", "secure", "update", "login", "account", "confirm",
    "bank", "signin", "webscr",
]
IP_REGEX = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")


def score_url(raw_url: str) -> dict:
    score = 0
    reasons = []

    url = raw_url if re.match(r"^https?://", raw_url) else f"http://{raw_url}"
    try:
        parsed = urlparse(url)
        host = parsed.hostname or ""
    except ValueError:
        return {
            "risk_score": 50,
            "risk_level": "suspicious",
            "category": "Malformed URL",
            "reasons": ["URL could not be parsed — treat with caution"],
            "recommendation": "Proceed with caution — verify through an official channel before acting on it.",
        }

    if IP_REGEX.match(host):
        score += 30
        reasons.append("Uses a raw IP address instead of a domain name")

    if parsed.scheme != "https":
        score += 15
        reasons.append("Does not use HTTPS encryption")

    subdomain_count = host.count(".") - 1
    if subdomain_count > 2:
        score += 15
        reasons.append(f"Unusually high number of subdomains ({subdomain_count})")

    if len(raw_url) > 75:
        score += 10
        reasons.append("Unusually long URL")

    if any(s in host for s in SHORTENERS):
        score += 20
        reasons.append("Uses a URL shortener, which hides the real destination")

    hits = [w for w in SUSPICIOUS_WORDS if w in raw_url.lower()]
    if hits:
        score += len(hits) * 8
        reasons.append(f"Suspicious keywords in the URL ({', '.join(hits[:3])})")

    if "@" in raw_url:
        score += 20
        reasons.append('Contains an "@" symbol — a known cloaking technique')

    if host.startswith("xn--"):
        score += 15
        reasons.append("Uses punycode encoding, sometimes used to spoof lookalike domains")

    score = min(100, score)
    if not reasons:
        reasons.append("No structural red flags found in the URL")

    risk_level = "dangerous" if score >= 65 else "suspicious" if score >= 30 else "safe"
    category = (
        "Suspicious URL / Phishing" if score >= 65
        else "Low-confidence URL risk" if score >= 30
        else "Legitimate-looking URL"
    )
    recommendation = {
        "dangerous": "Do not visit this link or enter any information on it. Report and delete.",
        "suspicious": "Proceed with caution — verify through an official channel before visiting.",
        "safe": "No major structural red flags. Still avoid entering sensitive info unless you're sure.",
    }[risk_level]

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "category": category,
        "reasons": reasons,
        "recommendation": recommendation,
    }
