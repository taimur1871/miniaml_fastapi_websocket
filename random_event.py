"""
generate a random event for websockets
"""
import time
import websockets

for i in range(3):
    time.sleep(3)
    r = websockets.connect('ws://localhost:9010/ws-2')
    print(r.ws_client.state)
