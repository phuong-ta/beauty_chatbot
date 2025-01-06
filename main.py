from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from services.chatbot import chatbot

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"response": "OK La"}
    )


class Message(BaseModel):
    message: str


@app.post("/chat", status_code=status.HTTP_201_CREATED)
async def send_message(message: Message):
    result = chatbot(message.message)
    #print(result)
    return result
