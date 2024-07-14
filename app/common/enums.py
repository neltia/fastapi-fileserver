# common/enums.py
from enum import Enum


class ResponseCodeEnum(str, Enum):
    SUCCESS = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500
