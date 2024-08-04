from pydantic import BaseModel


class FilesDownloadRequest(BaseModel):
    file_list: list
    zip_name: str = None
    password: str = "1234"
