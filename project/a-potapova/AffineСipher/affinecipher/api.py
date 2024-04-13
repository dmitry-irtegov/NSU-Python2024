from uvicorn.config import logger
from fastapi import FastAPI

from affinecipher.core.ciphers import AffineCipher
from affinecipher.language import define_language

ac_server = FastAPI(title="AffineCipher Server", version="0.1.0")


@ac_server.get("/encode", response_model=str)
async def encode(text: str, key: str = ""):
    encoded_text = AffineCipher(define_language(text)).encrypt(text, key=key)
    return encoded_text


@ac_server.get("/decode", response_model=str)
async def decode(text: str, key: str = ""):
    decoded_text = AffineCipher(define_language(text)).decrypt(text, key=key)
    return decoded_text


@ac_server.get("/health")
def health() -> str:
    logger.info("Health check")
    return "Server is running!"
