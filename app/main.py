from fastapi import FastAPI

from app.api.v1.routes_mock import router as mock_router
from app.schema.response import HealthResponse

app = FastAPI(title='Mock Service', version='1.0.0')

app.include_router(router=mock_router, prefix='/api/v1')


@app.get('/healthz', response_model=HealthResponse)
async def healthz() -> HealthResponse:
    """Liveness probe for K8s."""
    return HealthResponse()


@app.get('/readyz', response_model=HealthResponse)
async def readyz() -> HealthResponse:
    """Readiness probe for K8s."""
    return HealthResponse()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', host='0.0.0.0', port=7641, reload=True)
