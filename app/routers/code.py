from fastapi import APIRouter, HTTPException, status

from app.core.dependencies import get_code_assistant_service
from app.schemas.code import CodeRequest, CodeResponse

from app.services.history_service import HistoryService

router = APIRouter(prefix="/api", tags=["CodeScribe"])


@router.post("/comment", response_model=CodeResponse)
async def comment_code(payload: CodeRequest):
    if not payload.code.strip():
        raise HTTPException(status_code=400, detail="Le code ne peut pas être vide.")

    result = await get_code_assistant_service().comment_code(
        payload.code,
        payload.comment_level,
        payload.max_comment_length
    )

    HistoryService().add_entry("comment", payload.code, result)
    return CodeResponse(action="comment", result=result)


@router.post("/control", response_model=CodeResponse)
async def control_code(payload: CodeRequest):
    result = await get_code_assistant_service().control_code(
        payload.code,
        payload.check_syntax,
        payload.check_performance,
        payload.check_security,
        payload.check_best_practices
    )

    HistoryService().add_entry("control", payload.code, result)
    return CodeResponse(action="control", result=result)


@router.post("/compress", response_model=CodeResponse)
async def compress_code(payload: CodeRequest):
    result = await get_code_assistant_service().compress_code(
        payload.code,
        payload.compression_level
    )

    HistoryService().add_entry("compress", payload.code, result)
    return CodeResponse(action="compress", result=result)

@router.get("/history")
async def get_history():
    return HistoryService().get_history()