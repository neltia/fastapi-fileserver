from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from fastapi import UploadFile

from app.common.models.response_result import ResponseResult
from app.common.enums import ResponseCodeEnum
from app.file.models.upload_response import ret_file_info

from pathlib import Path
import hashlib
import os


# Directory to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_file_list():
    data = os.listdir(UPLOAD_DIR)
    result = ResponseResult(result_code=ResponseCodeEnum.SUCCESS, data=data, exclude_unset=True)
    return result


def upload_file(file: UploadFile):
    hash_sha256 = hashlib.sha256(file.file.read()).hexdigest()

    file_location = Path(UPLOAD_DIR) / hash_sha256
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    data = ret_file_info(file, hash_sha256, file_location)
    result = ResponseResult(result_code=ResponseCodeEnum.SUCCESS, data=data)
    return result


def download_file(file_hash):
    file_path = Path(UPLOAD_DIR) / file_hash
    if not file_path.exists():
        raise HTTPException(status_code=404)

    return FileResponse(path=file_path, filename=file_hash)
