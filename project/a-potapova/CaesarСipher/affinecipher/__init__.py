import uvicorn


def entrypoint() -> None:
    uvicorn.run("affinecipher.api:ac_server", host="localhost", port=8000, reload=True)

