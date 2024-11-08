from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

index_router = APIRouter()




@index_router.get("/")
async def main_page():
    return {"message": "Hello from main page"}
    #return templates.TemplateResponse("index.html")
