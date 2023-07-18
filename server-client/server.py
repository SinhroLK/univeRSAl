import socket
import threading
import random
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime

FORMAT = 'utf-8'
HEADER = 1024
serverPort = 5051
serverName = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen()


def smallE(conn):
    print("Configuring Small E attack")
    e = 3
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    msg = bytes("Programski jezici", encoding=FORMAT)
    pt = bytes_to_long(msg)
    ct = pow(pt, e, n)
    print(e)
    print(n)
    print(ct)
    print(1)
    conn.send((str(e)).encode(FORMAT))
    print(2)
    conn.send((str(n)).encode(FORMAT))
    print(3)
    conn.send((str(ct)).encode(FORMAT))
    print(4)

def hastad(conn):
    pass


def commonModulus(conn):
    pass


def wiener(conn):
    pass


def boneh(conn):
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
        msg = input("Choose your desired configuration ")
        # msg = random.randint(1, 5)
        match msg:
            case "1":
                smallE(connection)
            case "2":
                hastad(connection)
            case "3":
                commonModulus(connection)
            case "4":
                wiener(connection)
            case "5":
                boneh(connection)
            case _:
                print("Unknown configuration, please choose an existing one")


if __name__ == "__main__":
    print('Server is ready')
    while True:
        try:
            connectionSocket, address = serverSocket.accept()
            thread_main = threading.Thread(target=configure, args=(connectionSocket, address,))
            thread_main.start()
        except:
            print("Server killed")
