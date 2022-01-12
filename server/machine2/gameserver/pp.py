import asyncio
import time
import websockets
import json
from threading import Timer
import grpc
import dispatcher_pb2
import dispatcher_pb2_grpc


coroutine_timer=None

host = ""
port = ""

websocketsList = []
movesHistory=[]
currentFen = ""
startFen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

white_player = None
black_player = None
white_player_ID = ""
black_player_ID = ""
firstPlayerName="UNKNOWN"
secondPlayerName="UNKNOWN"

firstClockTime=60
secondClockTime=60

firstPlayerTurn=True
secondPlayerTurn=False

currentTurn="white"
isEnded=False


def close_game():
    with grpc.insecure_channel('51.250.18.255:8080') as channel:
        stub = dispatcher_pb2_grpc.DispatcherStub(channel)
        user = dispatcher_pb2.User(
            uuid=white_player_ID,
            name=f'Player_{white_player_ID[:8]}'
        )
        game = dispatcher_pb2.Game(
            owner=user,
            state=0,
            address=host,
            port=str(port)
        )
        response = stub.CloseGame(game)
    print(f'Received close_game response: {response.text}')


async def time_function():
    global firstClockTime
    global secondClockTime
    global currentTurn
    while firstClockTime > 0 and secondClockTime > 0:
        if (currentTurn == "white"):
            firstClockTime -= 1
            data={"firstClockTime": firstClockTime,
                  "secondClockTime": secondClockTime,
                  "type": "Time"}
        else:
            secondClockTime -= 1
            data = {"firstClockTime": firstClockTime,
                    "secondClockTime": secondClockTime,
                    "type": "Time"}
        print("Timer tick")
        for wbs in websocketsList:
            await sendToSocket(wbs, json.dumps(data))
        await asyncio.sleep(1)

def time_counter():
    asyncio.run(time_function())

async def initPlayer(websocket, user_id):
    global white_player
    global black_player
    global white_player_ID
    global black_player_ID
    global firstPlayerName
    global secondPlayerName
    global coroutine_timer
    data={}

    if white_player is None and white_player_ID == "":
        white_player= websocket
        white_player_ID= user_id
        firstPlayerName = f"Player_{user_id[:8]}"
        data={"type":"Init",
              "firstPlayerName":firstPlayerName,
              "playerType":"first",
              "currentFen":startFen}

        await sendToSocket(websocket,json.dumps(data))

    elif black_player is None and black_player_ID=="" and white_player_ID!=user_id:
        secondPlayerName=f"Player_{user_id[:8]}"
        data={"type":"Init",
              "firstPlayerName":secondPlayerName,
              "playerType":"second",
              "currentFen":startFen}
        black_player=websocket
        black_player_ID=user_id
        await sendToSocket(websocket,json.dumps(data))



        #Вход второго игрока
        data={"type":"PlayerIn",
              "firstPlayerName":firstPlayerName,
              "secondPlayerName":secondPlayerName}
        #await sendToSocket(websocket,json.dumps(data))
        #if (white_player!=None):
            #await sendToSocket(white_player,json.dumps(data))
        
        for wbs in websocketsList:
            await sendToSocket(wbs,json.dumps(data))

        #time_counter()
        #await timer()
        coroutine_timer= Timer(1,time_counter)
        coroutine_timer.start()
        #Timer().cancel()

    elif white_player is None and white_player_ID==user_id:
        white_player=websocket
        data={ "type":"Reconnect",
               "playerType":"first",
               "firstPlayerName":firstPlayerName,
               "secondPlayerName":secondPlayerName,
               "firstPlayerTurn":firstPlayerTurn,
               "secondPlayerTurn":secondPlayerTurn,
               "currentFen":currentFen,
               "movesHistory":movesHistory,
               "firstClockTime": firstClockTime,
               "secondClockTime": secondClockTime,
               "currentTurn": currentTurn,
               "isWaiting": currentTurn=="black",
               "currentOrientation":"white",
               "gameStarted": white_player_ID!="" and black_player_ID!=""
             }
        #if (black_player!=None):
            #await sendToSocket(black_player,json.dumps(data))
        await sendToSocket(websocket,json.dumps(data))
        
    elif black_player is None and black_player_ID==user_id:
        black_player=websocket
        data={ "type":"Reconnect",
               "playerType": "second",
               "firstPlayerName":secondPlayerName,
               "secondPlayerName":firstPlayerName,
               "firstPlayerTurn":secondPlayerTurn,
               "secondPlayerTurn":firstPlayerTurn,
               "currentFen":currentFen,
               "movesHistory": movesHistory,
               "firstClockTime": firstClockTime,
               "secondClockTime": secondClockTime,
               "currentTurn": currentTurn,
               "isWaiting": currentTurn=="white",
               "currentOrientation":"black",
               "gameStarted": white_player_ID != "" and black_player_ID != ""
             }
        #if (white_player!=None):
            #await sendToSocket(white_player,json.dumps(data))
        await sendToSocket(websocket,json.dumps(data))
    else:
        data={"type":"Init",
              "firstPlayerName":firstPlayerName,
              "secondPlayerName":secondPlayerName,
              "movesHistory":movesHistory,
              "firstClockTime":firstClockTime,
              "secondClockTime":secondClockTime,
              "playerType":"viewer",
              "gameStarted":white_player_ID != "" and black_player_ID != "",
              "firstPlayerTurn":firstPlayerTurn,
              "secondPlayerTurn":secondPlayerTurn,
              "currentFen":currentFen}
        await sendToSocket(websocket, json.dumps(data))


    
    #await websocket.send(json.dumps(data))


async def move(websocket,message):
    global isEnded
    global currentFen
    global movesHistory
    isEnded=message['isEnded']
    currentFen=message['currentFen']
    movesHistory=message['movesHistory']

    data={"type":"Move",
          "isEnded":isEnded,
          "currentFen":currentFen,
          "movesHistory":movesHistory}

    for wbs in websocketsList:
        if wbs!=websocket:
            await sendToSocket(wbs,json.dumps(data))


async def timeOut(websocket,message):
    data={"type":"Timeout"}
    for wbs in websocketsList:
        if wbs!=websocket:
            await sendToSocket(wbs,json.dumps(data))


async def timeDecrease(websocket,message):
    global firstClockTime
    global secondClockTime
    firstClockTime=message['firstClockTime']
    secondClockTime=message['secondClockTime']



async def sendToSocket(websocket, message):
    if (websocket!=None):
        await websocket.send(message)


async def produce(websocket, message):
    for ws in websocketsList:
        async with ws:
            await ws.send(message)
            await ws.recv()


async def consumer(websocket, message):
    global currentFen
    if (not message['isViewer'] and message['fen'] != startFen):
        currentFen = message['fen']
    for ws in websocketsList:
        await ws.send(currentFen)


async def handler(websocket, path):
    global white_player
    global black_player
    global firstPlayerTurn
    global secondPlayerTurn
    global firstClockTime
    global secondClockTime
    global currentTurn
    global coroutine_timer
    while True:
        if not websocketsList.__contains__(websocket):
            websocketsList.append(websocket)
        try:
            message = await websocket.recv()
            message = json.loads(message)
            if (message['type'] == "Init"):
                await initPlayer(websocket, message['user'])
            elif (message['type']=="Move"):
                firstPlayerTurn= not firstPlayerTurn
                secondPlayerTurn=not secondPlayerTurn
                #coroutine_timer.cancel()
                #coroutine_timer.start()
                if currentTurn=="white":
                    firstClockTime+=5
                    currentTurn="black"
                else:
                    secondClockTime+=5
                    currentTurn="white"
                await move(websocket,message)
                #дописать
            elif (message['type']=="Time"):
                print("TimeTick")
                await timeDecrease(websocket,message)
                #дописать
            elif (message['type']=="Timeout"):
                pass
                #дописать
            elif (message['type']=="Leave"):
                pass
            elif (message['type']=="GameOver"):
                time.sleep(5)
                close_game()
                exit()
                #дописать
        except (websockets.ConnectionClosedOK,websockets.ConnectionClosedError):
            if (white_player == websocket):
                white_player = None
            if (black_player == websocket):
                black_player = None
            websocketsList.remove(websocket)
            print("Someone disconnected")
            break
        
        #except websockets.ConnectionClosedOK:
        #    if (white_player == websocket):
        #        white_player = None
        #    if (black_player == websocket):
        #        black_player = None
        #    websocketsList.remove(websocket)
        #    print("Oops")
        #    break


async def main(h, p):
    global host
    global port
    host = h
    port = p
    async with websockets.serve(handler, host, port):
        await asyncio.Future()  # run forever


def start(host, port):
    print("Starting Room...")
    asyncio.run(main(host, port))
