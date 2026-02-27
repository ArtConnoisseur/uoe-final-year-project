from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.services.eeg import EEGReader
from app.routers import ws

@asynccontextmanager
async def lifespan(app: FastAPI):
    with EEGReader() as eeg_reader:
        app.state.eeg = eeg_reader
        yield

app = FastAPI(
    lifespan = lifespan
)

allowed_origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = allowed_origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(ws.router)
