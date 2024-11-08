from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

chatbot_router = APIRouter()


@chatbot_router.get("/chatbot")
async def show_chat_log():
    return [{"username": "Rick"}, {"username": "Morty"}]
