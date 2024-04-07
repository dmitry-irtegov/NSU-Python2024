import uvicorn


def entrypoint() -> None:
    uvicorn.run("caesarcipher.api:cc_server", host="0.0.0.0", port=8000, reload=True)

