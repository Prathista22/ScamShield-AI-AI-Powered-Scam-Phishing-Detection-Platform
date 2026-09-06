from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """Simple liveness check used by the frontend and for demo purposes."""
    return {"status": "ok"}
