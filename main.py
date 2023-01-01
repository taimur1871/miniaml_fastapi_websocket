# python 3.8.10

'''
Try to create and close websocket connection
'''

from time import sleep
from typing import Text
from fastapi import FastAPI, WebSocket, Request, websockets
from fastapi.responses import HTMLResponse, FileResponse
from starlette.websockets import WebSocketClose, WebSocketDisconnect
import uvicorn
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta
import time


templates = Jinja2Templates(directory="templates/")

app = FastAPI()
favicon_path = 'favicon.ico'


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("websocket.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    start_time = datetime.now()
    try:
        # send operations
        time.sleep(3)
        print('data sent')
    except WebSocketDisconnect:
        await websocket.close()
        print("Closed ws connection")

@app.websocket("/ws-2")
async def websocket_endpoint(websocket: WebSocket):
    count = 0
    await websocket.accept()
    try:
        while count < 2:
            time.sleep(1)
            await websocket.send_json({"hello": "world"})
            count += 1
            print(count)
        await websocket.close()
        print('Closed connection')
    except WebSocketDisconnect:
        await websocket.close()
        print("Closed connection")


@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)


@app.get('/conn', response_model=str)
async def conn():
    message = 'Connection established'
    return message
