from fastapi import FastAPI, Request
import asyncio
import time
import traceback
import uvicorn
import uuid
import datetime


from pydantic import BaseSettings
from typing import Any




from .api.v1.router import router as v1



class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "BFF-Web AeroAlpes"}

app = FastAPI(**app_configs)



app.include_router(v1, prefix="/v1")