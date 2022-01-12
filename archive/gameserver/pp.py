
import asyncio
import logging
import websockets
import json
from sys import argv



websocketsList=[]
movesHistory=[]
currentFen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
startFen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
whiteTimeStart=0
blackTimeStart=0
players=0

white_player=None
black_player=None
white_player_ID=""
black_player_ID=""


async def initPlayer(websocket,user_id):
    global white_player
    global black_player
    global white_player_ID
    global black_player_ID
    global movesHistory
    global players
    if white_player==None and(white_player_ID=="" or white_player_ID==user_id):
        white_player = websocket
        white_player_ID=user_id

<<<<<<< HEAD
        data={
            "status":"false",
            "orientation":"white",
            "fen":currentFen,
            'messageType':'Init',
            'movesHistory': movesHistory
=======
        data = {
            "status": "false",
            "orientation": "white",
            'fen':currentFen
>>>>>>> 13d41b35a75d2ad9c42b88f366cd730a218205c7
        }
        players+=1
        await websocket.send(json.dumps(data))
        data={
            'messageType':"Waiting",
        }
        if players==2:
            await produce(websocket,json.dumps(data))
    elif black_player==None and (black_player_ID=="" or black_player_ID==user_id):
        black_player=websocket
        black_player_ID=user_id
        data = {
            "status": "false",
            "orientation": "black",
            "fen": currentFen,
            'messageType':'Init',
            'movesHistory':movesHistory
        }
        black_player=websocket
        black_player_ID=user_id
        players+=1
        await websocket.send(json.dumps(data))
        data={
            'messageType':"Waiting",
        }
        if players==2:
            await produce(websocket,json.dumps(data))
    else:
        data = {
            "status": "true",
            "orientation": "white",
            "fen": currentFen,
            'messageType':'Init',
            'movesHistory': movesHistory
        }
        await websocket.send(json.dumps(data))



async def removeRoom():
    print("Room Destroyed")
    exit()

async def SetTimer(orientation,time):
    global white_player
    global black_player
    global whiteTimeStart
    global blackTimeStart
    if (orientation=="white" and whiteTimeStart==0):
        whiteTimeStart=time
    elif (orientation=="black" and blackTimeStart==0):
        blackTimeStart=time
    print ("whiteTime: " + str(whiteTimeStart))
    print ("blacktime: " + str(blackTimeStart))


async def sendToSocket(websocket,message):
    async with websocket:
        await websocket.send(message)

async def produce(websocket, message):
    print("sending")
    for ws in websocketsList:
        await ws.send(message)


async def consumer(websocket,message):
    global currentFen
    global movesHistory
    print(message['fen'])
    if (message['fen']!=startFen):
        currentFen=message['fen']
        if (len(movesHistory)<len(message['history'])):
            movesHistory=message['history']
    for ws in websocketsList:
        print('sending message')
        if (ws!=websocket):
            data={'fen':currentFen,
                'messageType':'Move',
                 'movesHistory':movesHistory
                }
            await ws.send(json.dumps(data))


async def handler(websocket, path):
    global white_player
    global black_player
    global movesHistory
    while True:
        if not websocketsList.__contains__(websocket):
            websocketsList.append(websocket)
        try:
            message = await websocket.recv()
            print(message)
            print(movesHistory)
            message=json.loads(message)

            if (message['messageType']=="Init"):
                await initPlayer(websocket,message['user_id'])
            elif (message['messageType']=="GameOver"):
                await removeRoom()
            elif (message['messageType']=="Timer"):
                await SetTimer(message['orientation'],message["time"])
            else:
                print(message)
                await consumer(websocket, message)
        except websockets.ConnectionClosedOK:
            if (white_player==websocket):
                white_player=None
            if (black_player==websocket):
                black_player=None
            websocketsList.remove(websocket)
            print("Oops")
            break


async def main(host,port):
    async with websockets.serve(handler, host,port):
        await asyncio.Future()  # run forever


def start(host, port):
    print("Starting Room...")
    asyncio.run(main(host, port))

<<<<<<< HEAD
start("localhost",5001)
=======
start("localhost",50051)
>>>>>>> 13d41b35a75d2ad9c42b88f366cd730a218205c7
