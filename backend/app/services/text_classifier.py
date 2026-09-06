"""
Text risk scoring service.

This starter version uses weighted keyword matching so the API is fully
functional out of the box. Member 3 should replace `score_text()`'s internals
with a call to the trained TF-IDF + Logistic Regression model saved by
`ml/train.py` (see the commented-out loading code at the bottom of this file).
"""
import re

KEYWORD_WEIGHTS = {
    "Prize / Lottery Scam": [
        "won", "winner", "congratulations", "claim your reward",
        "lucky draw", "lottery", "prize", "cash reward", "selected",
    ],
    "Banking / Financial Scam": [
        "account suspended", "verify your account", "bank account", "kyc",
        "otp", "blocked", "unusual activity", "update your details",
        "net banking", "debit card", "credit card",
    ],
    "Job Scam": [
        "work from home", "earn per day", "job offer", "part time job",
        "no experience needed", "hiring now", "easy money", "recruitment",
    ],
    "Investment Scam": [
        "guaranteed returns", "double your money", "crypto investment",
        "trading profit", "invest now", "high returns", "stock tips",
    ],
    "Delivery Scam": [
        "parcel", "delivery failed", "customs fee", "shipment", "courier",
        "reschedule delivery", "pending package",
    ],
    "Account / Password Scam": [
        "password expired", "click to reset", "account locked",
        "confirm your identity", "unusual login", "suspicious login attempt",
    ],
    "Romance / Social Engineering": [
        "lonely", "deployed overseas", "need money urgently", "love you",
        "soulmate", "send gift card",
    ],
}

URGENCY_TERMS = [
    "immediately", "urgent", "act now", "within 24 hours", "limited time",
    "final notice", "failure to respond", "last chance", "expire",
]

REQUEST_TERMS = [
    "click this link", "click here", "provide your", "enter your pin",
    "share your otp", "send your bank details", "verify now",
]

LINK_REGEX = re.compile(r"(https?://\S+|www\.\S+)", re.IGNORECASE)


def score_text(raw_text: str) -> dict:
    text = raw_text.lower()
    score = 0
    reasons = []
    category_hits = {}

    for category, terms in KEYWORD_WEIGHTS.items():
        hits = sum(1 for term in terms if term in text)
        if hits:
            category_hits[category] = hits
            score += hits * 14

    urgency_hits = [t for t in URGENCY_TERMS if t in text]
    if urgency_hits:
        score += len(urgency_hits) * 10
        reasons.append(f'Urgency-pressure language detected ("{urgency_hits[0]}")')

    request_hits = [t for t in REQUEST_TERMS if t in text]
    if request_hits:
        score += len(request_hits) * 12
        reasons.append("Asks you to click a link or hand over sensitive info")

    if LINK_REGEX.search(raw_text):
        score += 10
        reasons.append("Contains an embedded external link")

    top_category = "Legitimate"
    top_hits = 0
    for category, hits in category_hits.items():
        if hits > top_hits:
            top_hits, top_category = hits, category

    if top_category != "Legitimate":
        reasons.insert(0, f'Vocabulary strongly matches known "{top_category}" patterns')

    score = min(100, score)
    if not reasons:
        reasons.append("No scam vocabulary, urgency language, or suspicious requests found")

    risk_level = "dangerous" if score >= 65 else "suspicious" if score >= 30 else "safe"
    recommendation = {
        "dangerous": "Do not click, reply, or share personal/financial info. Delete or report this message.",
        "suspicious": "Proceed with caution — verify through an official channel before acting on it.",
        "safe": "No major risk indicators found. Still stay alert for later requests for money or details.",
    }[risk_level]

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "category": top_category,
        "reasons": reasons,
        "recommendation": recommendation,
    }


# --- Swap-in point for the trained ML model -------------------------------
#
# import joblib
# _vectorizer = joblib.load("ml/vectorizer.pkl")
# _model = joblib.load("ml/model.pkl")
#
# def score_text_ml(raw_text: str) -> dict:
#     X = _vectorizer.transform([raw_text])
#     proba = _model.predict_proba(X)[0]
#     predicted_class = _model.classes_[proba.argmax()]
#     confidence = int(proba.max() * 100)
#     ...
