from fastapi import FastAPI
from contextlib import asynccontextmanager
from services.eeg import EEGReader

@asynccontextmanager
async def lifespan(app: FastAPI):
    with
