from uvicorn.config import logger
from fastapi import FastAPI

cc_server = FastAPI(title="CaesarCipher Server", version="0.1.0")


@cc_server.get("/health")
def health() -> str:
    logger.info("Health check")
    return "Server is running!"
