import socket
import threading
import random
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
from sentences import sentences

FORMAT = 'utf-8'
HEADER = 100000
serverPort = 5060
serverName = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen()


def smallE(conn):
    print("Configuring Small e attack")
    e = 3
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    pt = sentences[random.randint(0, 19)]
    msg = bytes(pt, encoding=FORMAT)
    decr = bytes_to_long(msg)
    ct = pow(decr, e, n)
    print("Plaintext: ", pt)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    string = str(e) + "." + str(n) + "." + str(ct)
    conn.send(string.encode(FORMAT))


def hastad(conn):
    print("Configuring Hastad's attack")
    e = random.randint(4, 20)
    message = sentences[random.randint(0, 19)]
    n = []
    ct = []
    decr = bytes(message, encoding=FORMAT)
    for i in range(e):
        p = getPrime(1024)
        q = getPrime(1024)
        n.append(p * q)
        ct.append(pow(bytes_to_long(decr), e, n[i]))
    print("Plaintext: ", message)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    string = str(e) + "."
    for i in range(e):
        string = string + str(n[i]) + "." + str(ct[i]) + "."
    conn.send(string.encode(FORMAT))


def commonModulus(conn):
    pass


def wiener(conn):
    print("Configuring Wiener's attack")
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        d = getPrime(256)
        e = pow(d, -1, phi)
        if e.bit_length() >= n.bit_length():
            break
    pt = sentences[random.randint(0, 19)]
    message = bytes(pt, encoding=FORMAT)
    msg = bytes_to_long(message)
    ct = pow(msg, e, n)
    string = str(e) + "." + str(n) + "." + str(ct)
    print("Plaintext: ", message)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    conn.send(string.encode(FORMAT))


def sumOPrimes(conn):
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
        print("5. Sum O Primes")
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
                sumOPrimes(connection)
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
