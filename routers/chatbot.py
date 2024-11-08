from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

chatbot_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@chatbot_router.get("/chatbot", response_class=HTMLResponse)
async def chatbot_page(request: Request):
    return {"message": "chatbot page"}
    """
    return templates.TemplateResponse(
        request=request, name="chatbot.html", context={"response": "ok"}
    )
    """


class FormRequest(BaseModel):
    message: str


@chatbot_router.post("/chatbot/", status_code=status.HTTP_201_CREATED)
async def upload_message(request: FormRequest):
    message = request.message
    return message