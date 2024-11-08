import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.index import main_router
from routers.chatbot import chatbot_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main_router)
app.include_router(chatbot_router)
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

