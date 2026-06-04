from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/ping")
async def ping():
    return {"status": "ok"}


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "app": "CodeScribe"
    }