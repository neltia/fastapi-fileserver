from fastapi import FastAPI
from app.file import file_controller
from app.common.handlers.error_handler import setup_exception_handlers

app = FastAPI()

# exception
setup_exception_handlers(app)

# router
app.include_router(file_controller.router, prefix="/file", tags=["File"])
