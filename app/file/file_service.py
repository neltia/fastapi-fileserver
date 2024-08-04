from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from fastapi import UploadFile

from app.common.models.response_result import ResponseResult
from app.common.enums import ResponseCodeEnum
from app.file.models.upload_response import ret_file_info

from pathlib import Path
import hashlib
import os
import zipfile
from datetime import datetime


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

    media_type = "application/octect-stream"
    return FileResponse(path=file_path, filename=file_hash, media_type=media_type)


def download_files_withzip(hash_list, zip_name, password):
    # zip name
    if zip_name is None:
        zip_name = datetime.now().strftime("%Y%m%d_%H%M%S_fastapi_downloaded")
    zip_name = zip_name + ".zip"
    zip_path = zip_name

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_hash in hash_list:
            file_path = Path(UPLOAD_DIR) / file_hash
            if not file_path.exists():
                raise HTTPException(status_code=404)

            find_file_path = os.path.join(UPLOAD_DIR, file_hash)
            f = open(find_file_path, "rb")
            data = f.read()
            f.close()

            with open(find_file_path, "wb") as f:
                f.write(data)
            zipf.write(find_file_path, arcname=file_hash)

    # ret download response
    media_type = "application/zip"
    return FileResponse(path=zip_path, filename=zip_name, media_type=media_type)
