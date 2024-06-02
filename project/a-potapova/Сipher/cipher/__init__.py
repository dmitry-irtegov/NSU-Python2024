import uvicorn


def entrypoint() -> None:
    uvicorn.run("cipher.api:cipher_app", host="localhost", port=8000, reload=True)