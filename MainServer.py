
import asyncio
import logging
import websockets
import subprocess
import json
import socket
from subprocess import Popen, CREATE_NEW_CONSOLE
import multiprocessing
import sys
from PP import start

host="localhost"
port=5002
roomsAmount=0

server_host='localhost'
server_port=6543


serverList=[]


def hello():
    print("HELLO")


def createRoom(host,port):
    multiprocessing.Process(target=start, args=(host,port)).start()
    print('started')
    #theproc = subprocess.run(["D:\\pythonProject1\\venv\\Scripts\\python", "PP.py",'&'])
    #theproc.communicate()


def startMainServer():
    global port
    global host
    global roomsAmount
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((server_host,server_port))
    sock.listen(1)
    conn, addr = sock.accept()

    print ('connected:', addr)

    while True:
        data = conn.recv(1024)
        data=data.decode("utf-8")
        if not data:
            break
        if (data=="CREATE ROOM"):
            port += 1
            roomsAmount += 1
            createRoom(host,port)
            createRoom(host, port+3)
            conn.send(json.dumps({"host":host, "port":port}).encode())

    conn.close()


if __name__ == '__main__':
    startMainServer()
#Popen(['python', 'PP.py','localhost','5001'])
#asyncio.run(main())