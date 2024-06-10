from fastapi import APIRouter, Response, status

from cipher.dependencies import table_cipher_service
from cipher.settings import DECODE_REQUEST_TIMEOUT

router = APIRouter()


@router.get("/keygen", response_model=str)
def keygen(response: Response,
           language: str = "en"):
    try:
        return str(table_cipher_service.keygen(language))
    except ValueError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return e
    except BaseException as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return e


@router.get("/encode", response_model=str)
def encode(plaintext: str,
           response: Response,
           key: str = None):
    try:
        return table_cipher_service.encode(plaintext, key=key)
    except ValueError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return e
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return e


@router.get("/decode")
async def decode(ciphertext: str,
                 response: Response,
                 key: str = None,
                 timeout: float = DECODE_REQUEST_TIMEOUT) -> tuple[str, str] | str:
    try:
        plaintext, result_key, result_status = await table_cipher_service.decode(ciphertext, timeout, key=key)
        response.status_code = result_status
        return plaintext, result_key
    except ValueError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return str(e)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return str(e)


@router.get("/decode/read", response_model=tuple[str, str])
async def read_result(response: Response):
    try:
        plaintext, result_key, result_status = await table_cipher_service.read()
        response.status_code = result_status
        return plaintext, result_key
    except ValueError as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return str(e)


@router.get("/decode/stop", response_model=tuple[str, str])
async def stop_decode(response: Response):
    try:
        plaintext, result_key, result_status = await table_cipher_service.stop()
        response.status_code = result_status
        return plaintext, result_key
    except ValueError as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return str(e)
