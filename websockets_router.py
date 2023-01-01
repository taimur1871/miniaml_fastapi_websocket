"""
ws routers for the app
"""
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from datetime import datetime
import time

router = APIRouter()


@router.websocket("/ws")
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

@router.websocket("/ws-2")
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


@router.get('/conn', response_model=str)
async def conn():
    message = 'Connection established'
    return message
