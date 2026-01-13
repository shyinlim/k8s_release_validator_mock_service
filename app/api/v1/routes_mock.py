from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.schema.response import (
    OkResponse,
    BadResponse,
    SlowResponse,
    VersionResponse,
)
from app.service.mock_service import delay_response, get_version

router = APIRouter()


@router.get('/ok', response_model=OkResponse)
async def ok() -> OkResponse:
    """Return 200 ok."""
    return OkResponse


@router.get('/bad', response_model=BadResponse)
async def bad() -> BadResponse:
    """Return 400 bad request."""
    return JSONResponse(
        status_code=400,
        content=BadResponse.model_dump()
    )


@router.get('/slow', response_model=SlowResponse)
async def slow(ms: int = Query(default=500, ge=0, le=10000)) -> SlowResponse:
    """
    Return response after delay.

    Args:
        ms: Milliseconds to delay (0-10000).
    """

    delay = await delay_response(ms=ms)
    return SlowResponse(delay_ms=delay)


@router.get("/version", response_model=VersionResponse)
async def version() -> VersionResponse:
    """Return application version."""
    return VersionResponse(version=get_version())
