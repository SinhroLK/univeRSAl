import socket
import threading

FORMAT = 'utf-8'
HEADER = 1024
serverPort = 5051
serverName = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen()


def handleClient(connection, addr):
    while True:
        prom = connection.recv(HEADER).decode(FORMAT)
        print(prom)


if __name__ == "__main__":
    print('Server is ready')
    while True:
        connectionSocket, address = serverSocket.accept()
        thread_main = threading.Thread(target=handleClient, args=(connectionSocket, address,))
        thread_main.start()