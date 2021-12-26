import socket
import json

serversList=[]

serversList.append({"host":"localhost", "port":6543})
cur_server=0


def CreateRoom():
    index=cur_server
    sock = socket.socket()
    for i in range(0,len(serversList)):
        try:
            sock.connect((serversList[index]['host'],serversList[index]['port']))
            break
        except:
            index+=1
            index=divmod(index, len(serversList))

    sock.send('CREATE ROOM'.encode('utf-8'))

    data = sock.recv(1024)
    print(json.loads(data.decode("utf-8")))


    sock.close()

CreateRoom()