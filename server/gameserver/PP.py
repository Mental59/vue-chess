
import asyncio
import logging
import subprocess
import websockets
import json
from sys import argv


host=""
port=""



websocketsList=[]
currentFen=""
startFen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

white_player=None
black_player=None
white_player_ID=""
black_player_ID=""


async def initPlayer(websocket,user_id):
    global white_player
    global black_player
    global white_player_ID
    global black_player_ID
    if white_player==None and(white_player_ID=="" or white_player_ID==user_id):
        white_player = websocket
        white_player_ID=user_id

        data={
            "status":"false",
            "orientation":"white"
        }
        await websocket.send(json.dumps(data))
    elif black_player==None and (black_player_ID=="" or black_player_ID==user_id):
        black_player=websocket
        black_player_ID=user_id
        data = {
            "status": "false",
            "orientation": "black"
        }
        black_player=websocket
        black_player_ID=user_id
        await websocket.send(json.dumps(data))
    else:
        data = {
            "status": "true",
            "orientation": "white"
        }
        await websocket.send(json.dumps(data))

async def sendToSocket(websocket,message):
    async with websocket:
        await websocket.send(message)

async def produce(websocket, message):
    for ws in websocketsList:
        async with ws:
            await ws.send(message)
            await ws.recv()


async def consumer(websocket,message):
    global currentFen
    if (not message['isViewer'] and message['fen']!=startFen):
        currentFen=message['fen']
    for ws in websocketsList:
        await ws.send(currentFen)


async def handler(websocket, path):
    global white_player
    global black_player
    while True:
        if not websocketsList.__contains__(websocket):
            websocketsList.append(websocket)
        try:
            message = await websocket.recv()
            message=json.loads(message)
            if (message['messageType']=="Init"):
                await initPlayer(websocket,message['user_id'])
            else:
                await consumer(websocket, message)
        except websockets.ConnectionClosedOK:
            if (white_player==websocket):
                white_player=None
            if (black_player==websocket):
                black_player=None
            websocketsList.remove(websocket)
            print("Oops")
            break


async def main(h,p):
    global host
    host=h
    global port
    port=p
    async with websockets.serve(handler, host,port):
        await asyncio.Future()  # run forever

def start(host,port):
    print("Starting Room...")
    asyncio.run(main(host,port))