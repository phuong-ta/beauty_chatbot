import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.chatbot import chatbot_router
from routers.index import index_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(index_router)
app.include_router(chatbot_router)
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
