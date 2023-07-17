import threading
import socket
from random import randint

FORMAT = 'utf-8'
HEADER = 1024
serverPort = 5051
serverName = socket.gethostbyname(socket.gethostname())
username = ''
stop = False
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
def solver():
    while True:
        try:
            prom = input()
            clientSocket.send(prom.encode(FORMAT))
        except:
            print("deadge")

try:
    receive_thread = threading.Thread(target=solver)
    receive_thread.start()
except:
    print("Client closed")