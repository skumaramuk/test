from fastapi import FastAPI

from .routers import types

app = FastAPI()

app.include_router(types.router)


@app.get("/")
def root():
    return {"message": "Hello"}
