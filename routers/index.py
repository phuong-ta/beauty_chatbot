from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

main_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@main_router.get("/", response_class=HTMLResponse)
async def main_page():
    return {"message": "Hello from main page"}
    #return templates.TemplateResponse("index.html")
