from fastapi import APIRouter, UploadFile
from app.common.models.response_result import ResponseResult
from app.file.models.files_download_request import FilesDownloadRequest
from app.file import file_service

router = APIRouter()


@router.get("/list", response_model=ResponseResult)
async def get_file_list():
    result = file_service.get_file_list()
    return result


@router.post("/upload/", response_model=ResponseResult)
async def upload_file(file: UploadFile):
    result = file_service.upload_file(file)
    return result


# file download by sha256 hash string
@router.get("/download/{file_hash}")
async def download_file(file_hash: str):
    result = file_service.download_file(file_hash)
    return result


# file download by sha256 hash string list
@router.post("/download/files")
async def download_file_list(download_request: FilesDownloadRequest):
    hash_list = download_request.file_list
    zip_name = download_request.zip_name
    password = download_request.file_list
    result = file_service.download_files_withzip(hash_list, zip_name, password)
    return result
