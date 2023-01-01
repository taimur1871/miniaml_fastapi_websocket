"""
basic app info
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates/")
favicon_path = 'favicon.ico'
router = APIRouter()


@router.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("websocket.html", {"request": request})
