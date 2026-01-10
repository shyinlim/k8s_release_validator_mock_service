from pydantic import BaseModel


class OkResponse(BaseModel):
    status: str = 'ok'


class BadResponse(BaseModel):
    status: str = 'bad'
    message: str = 'This is bad request'


class SlowResponse(BaseModel):
    status: str = 'ok'
    delay_ms: int


class VersionResponse(BaseModel):
    version: str


class HealthResponse(BaseModel):
    status: str = 'healthy'
