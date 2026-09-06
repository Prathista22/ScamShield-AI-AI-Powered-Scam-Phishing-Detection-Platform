from fastapi import APIRouter

from app.schemas.analyze import TextAnalyzeRequest, UrlAnalyzeRequest, AnalyzeResponse
from app.services.text_classifier import score_text
from app.services.url_analyzer import score_url

router = APIRouter()


@router.post("/text", response_model=AnalyzeResponse)
def analyze_text(payload: TextAnalyzeRequest):
    result = score_text(payload.content)
    return AnalyzeResponse(**result)


@router.post("/url", response_model=AnalyzeResponse)
def analyze_url(payload: UrlAnalyzeRequest):
    result = score_url(payload.url)
    return AnalyzeResponse(**result)


# TODO (Member 4): add /image (OCR via pytesseract) and /qr (pyzbar decode)
# endpoints here, then feed the extracted text/URL back through score_text()
# / score_url() above and return an AnalyzeResponse with extracted_text set.
