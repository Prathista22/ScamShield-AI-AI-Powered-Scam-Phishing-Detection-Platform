"""
ScamShield AI — FastAPI entrypoint.

Run with:
    uvicorn app.main:app --reload --port 8000
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, analyze

app = FastAPI(
    title="ScamShield AI API",
    description="Scam & phishing risk-assessment API — text, URL, OCR, and QR analysis.",
    version="0.1.0",
)

# Allow the React dev server to call this API during development.
# Tighten this list before deploying anywhere public.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(analyze.router, prefix="/api/analyze", tags=["analyze"])


@app.get("/")
def root():
    return {"message": "ScamShield AI API is running. See /docs for endpoints."}
