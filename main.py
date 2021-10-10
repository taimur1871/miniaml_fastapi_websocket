# python 3.8.10

'''
Try to create and close websocket connection
'''

from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocketClose, WebSocketDisconnect
import uvicorn
from fastapi.templating import Jinja2Templates
import time


templates = Jinja2Templates(directory="templates/")


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        for i in range(3):
            #data = await websocket.receive_text()
            time.sleep(2)
            print('is it working')
            await websocket.send_json({"hello": "world"})
        await websocket.close()
        print('Closed connection')
    except WebSocketDisconnect:
        await websocket.close()
        print("Closed connection")
