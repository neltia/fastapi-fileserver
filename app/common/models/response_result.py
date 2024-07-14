# common/models/response.py
from pydantic import BaseModel, Field
from typing import Optional, Any
from app.common.enums import ResponseCodeEnum


class ResponseResult(BaseModel):
    result_code: ResponseCodeEnum
    result_msg: Optional[str] = Field(default=None)
    error_msg: Optional[str] = None
    data: Optional[Any] = None

    class Config:
        exclude_unset = True
        exclude_none = True
