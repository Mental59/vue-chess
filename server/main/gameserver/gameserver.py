
import asyncio
import logging
import websockets
import subprocess
import json
import socket
from subprocess import Popen
import multiprocessing
import sys
from pp import start


host = "0.0.0.0"
port = 5000
roomsAmount = 0

server_host = '0.0.0.0'
server_port = 6543
sock = None


def createRoom(host, port):
    multiprocessing.Process(target=start, args=(host, port)).start()
    print('started')


def startMainServer():
    global sock
    global port
    global host
    global roomsAmount

    conn, addr = sock.accept()

    print('connected:', addr)

    while True:
        data = conn.recv(1024)
        data = data.decode("utf-8")
        if not data:
            break
        if (data == "CREATE ROOM"):
            port += 1
            roomsAmount += 1
            createRoom(host, port)
            conn.send(json.dumps({"host": host, "port": str(port)}).encode())
    conn.close()


if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server_host, server_port))
        print('Bind successful')
    except socket.error as e:
        print('Error ocurred ')
    sock.listen(10)

    while(True):
        startMainServer()
