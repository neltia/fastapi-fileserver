# common/handlers/error_handler.py
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.common.models.response_result import ResponseResult
from app.common.enums import ResponseCodeEnum


def setup_exception_handlers(app):
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        response = ResponseResult(
            result_code=ResponseCodeEnum(exc.status_code),
            error_msg="not found"
        )
        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump(exclude_none=True)
        )

    @app.exception_handler(404)
    async def not_found_exception_handler(request: Request, exc):
        response = ResponseResult(
            result_code=ResponseCodeEnum.NOT_FOUND,
            message="Resource not found"
        )
        return JSONResponse(
            status_code=404,
            content=response.dict(exclude_none=True)
        )
