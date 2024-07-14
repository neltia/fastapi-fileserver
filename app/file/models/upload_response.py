import hashlib


def ret_file_info(file, hash_sha256, file_location):
    hash_md5 = hashlib.md5(file.file.read()).hexdigest()
    hash_sha1 = hashlib.sha1(file.file.read()).hexdigest()

    data = {
        "file_name": file.filename,
        "file_path": file_location,
        "file_size": file.size,
        "upload_type": file.content_type,
        "hash": {
            "md5": hash_md5,
            "sha1": hash_sha1,
            "sha256": hash_sha256
        }
    }
    return data
