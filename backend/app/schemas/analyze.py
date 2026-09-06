from typing import List, Optional
from pydantic import BaseModel, Field


class TextAnalyzeRequest(BaseModel):
    content: str = Field(..., min_length=1, description="Raw SMS/WhatsApp/email text")


class UrlAnalyzeRequest(BaseModel):
    url: str = Field(..., min_length=3)


class AnalyzeResponse(BaseModel):
    risk_score: int = Field(..., ge=0, le=100)
    risk_level: str  # "safe" | "suspicious" | "dangerous"
    category: str
    reasons: List[str]
    recommendation: str
    extracted_text: Optional[str] = None
