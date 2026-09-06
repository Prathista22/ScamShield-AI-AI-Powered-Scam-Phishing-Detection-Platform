"""Text cleaning utilities for the ScamShield AI NLP pipeline."""
import re

STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "to", "of",
    "in", "on", "for", "and", "or", "it", "this", "that", "with", "your",
    "you", "we", "our", "at", "by", "as", "from",
}


def clean_text(text: str) -> str:
    """Lowercase, strip URLs/punctuation/digits, and drop stopwords."""
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)   # strip URLs (kept as a separate feature elsewhere)
    text = re.sub(r"[^a-z\s]", " ", text)                 # strip punctuation & digits
    tokens = [t for t in text.split() if t and t not in STOPWORDS]
    return " ".join(tokens)
