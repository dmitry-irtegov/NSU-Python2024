from fastapi.exceptions import ResponseValidationError
from starlette import status
from starlette.responses import PlainTextResponse
from uvicorn.config import logger
from fastapi import FastAPI
import cipher.table.api as tablecipher_api

cipher_app = FastAPI(title="Cipher App", version="0.1.0")

cipher_app.include_router(tablecipher_api.router,
                          prefix="/tablecipher",
                          tags=["tablecipher"])


@cipher_app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


@cipher_app.get("/health")
def health() -> str:
    logger.info("Health check")
    return "Server is running!"
