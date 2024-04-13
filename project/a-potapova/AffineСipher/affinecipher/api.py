from uvicorn.config import logger
from fastapi import FastAPI

from affinecipher.core.ciphers import AffineCipher

ac_server = FastAPI(title="AffineCipher Server", version="0.1.0")


@ac_server.get("/encode", response_model=str)
async def encode(text: str, key: str = ""):
    encoded_text = AffineCipher(key=key).encrypt(text)
    return encoded_text


@ac_server.get("/decode", response_model=str)
async def decode(text: str, key: str = ""):
    decoded_text = AffineCipher(key=key).decrypt(text)
    return decoded_text


@ac_server.get("/health")
def health() -> str:
    logger.info("Health check")
    return "Server is running!"
