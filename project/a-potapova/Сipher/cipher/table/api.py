from fastapi import APIRouter, Response, status

from cipher.table.service import TableCipherService

router = APIRouter()


@router.get("/keygen", response_model=str)
def keygen(response: Response,
           language: str = "en"):
    try:
        return str(TableCipherService.keygen(language))
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
        return TableCipherService.encode(plaintext, key)
    except ValueError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return e
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return e


@router.get("/decode", response_model=tuple[str, str])
def decode(ciphertext: str,
           response: Response,
           key: str = None):
    try:
        return TableCipherService.decode(ciphertext, key)
    except ValueError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return e
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return e
