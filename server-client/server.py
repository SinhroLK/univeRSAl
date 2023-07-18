import socket
import threading
import random

FORMAT = 'utf-8'
HEADER = 1024
serverPort = 5051
serverName = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen()

def smallE():
    pass

def hastad():
    pass
def commonModulus():
    pass
def wiener():
    pass
def boneh():
    pass
def configure(connection, addr):
    print(f'New connection at {addr}')
    print(r"""                                          
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                                      
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                     
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌                                     
    ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌                                     
    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌                                     
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                     
    ▐░█▀▀▀▀█░█▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌                                     
    ▐░▌     ▐░▌            ▐░▌▐░▌       ▐░▌                                     
    ▐░▌      ▐░▌  ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌                                     
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌                                     
     ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀                                      
                                                                                
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
    ▐░▌          ▐░▌       ▐░▌▐░▌    ▐░▌         ▐░▌  ▐░▌          ▐░▌       ▐░▌
    ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
    ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌      ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀▀▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
              ▐░▌▐░▌       ▐░▌▐░▌        ▐░▌ ▐░▌      ▐░▌          ▐░▌     ▐░▌  
     ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄▐░▐░▌       ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌        ▐░░░░░░░░░░░▌▐░▌       ▐░▌
     ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀                                                                                                                                                                                                                    
                        """)
    while True:
        print("1. Small e attack")
        print("2. Hastad broadcast attack")
        print("3. Common modulus attack")
        print("4. Wiener attack")
        print("5. Boneh-Durfee Attack")
        msg = input("Choose your desired configuration")
        #msg = random.randint(1, 5)
        match msg:
            case "1": smallE()
            case "2": hastad()
            case "3": commonModulus()
            case "4": wiener()
            case "5": boneh()
            case _: print("Unknown configuration, please choose an existing one")


if __name__ == "__main__":
    print('Server is ready')
    while True:
        try:
            connectionSocket, address = serverSocket.accept()
            thread_main = threading.Thread(target=configure, args=(connectionSocket, address,))
            thread_main.start()
        except:
            print("Server killed")