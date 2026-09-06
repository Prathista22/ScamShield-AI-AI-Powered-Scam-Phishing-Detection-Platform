# ScamShield AI — System Architecture

```
React Frontend  ──▶  FastAPI Backend  ──▶  MySQL Database
     ▲                     │                    │
     └─────────────────────┘◀───────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
     NLP/ML Module   URL Risk Engine   OCR + QR Module
    (TF-IDF + LR)   (feature-based)   (Tesseract/pyzbar)
```

## Data flow

1. User submits text / URL / image via the React frontend.
2. Request hits a FastAPI endpoint under `/api/analyze/*`.
3. Router dispatches by input type:
   - **Text** → `services/text_classifier.py`
   - **URL** → `services/url_analyzer.py`
   - **Image** → OCR extracts text/URL → re-routed to the above
   - **QR** → decode → URL → `url_analyzer.py`
4. Result is persisted to `scan_history` in MySQL.
5. Response returned to the frontend as a risk card.
6. The dashboard reads aggregate stats from the DB for its charts.

## What's genuinely ML vs. traditional programming

- **ML**: TF-IDF vectorization + Logistic Regression classification of
  message category (`ml/train.py`, eventually swapped into
  `services/text_classifier.py`).
- **Traditional programming**: URL feature extraction, OCR invocation, QR
  decoding, risk-score aggregation, explanation-string generation.

Both are legitimate parts of the system — being upfront about which is which
is expected during the viva.

See the Review I presentation for the full blueprint (problem statement,
literature review, module breakdown, timeline, etc.).
