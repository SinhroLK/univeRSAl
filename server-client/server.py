import socket
import threading
import random
from Crypto.Util.number import bytes_to_long, getPrime, GCD
from sentences import sentences
from tqdm import tqdm

FORMAT = 'utf-8'
HEADER = 100000
serverPort = 5060
serverName = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen()


def smallE(conn: socket) -> None:
    print("Configuring Small e attack")
    e = 3
    for _ in tqdm(range(1), desc="Configuring"):
        p = getPrime(1024)
        q = getPrime(1024)
        n = p * q
        pt = sentences[random.randint(0, len(sentences) - 1)]
        message = bytes(pt, encoding=FORMAT)
        msg = bytes_to_long(message)
        ct = pow(msg, e, n)
    print("Plaintext: ", pt)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    string = str(e) + "." + str(n) + "." + str(ct)
    conn.send(string.encode(FORMAT))


def hastad(conn: socket) -> None:
    print("Configuring Hastad's attack")
    eList = [2, 3, 5, 7, 11, 13, 17, 19]
    e = eList[random.randint(0, len(eList) - 1)]
    pt = sentences[random.randint(0, len(sentences) - 1)]
    n = []
    ct = []
    message = bytes(pt, encoding=FORMAT)
    for i in tqdm(range(e), desc="Configuring"):
        p = getPrime(1024)
        q = getPrime(1024)
        n.append(p * q)
        ct.append(pow(bytes_to_long(message), e, n[i]))
    print("Plaintext: ", pt)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    string = str(e) + "."
    for i in range(e):
        string = string + str(n[i]) + "." + str(ct[i]) + "."
    conn.send(string.encode(FORMAT))


def commonModulus(conn: socket) -> None:
    for i in tqdm(range(1), desc="Configuring"):
        while True:
            e1 = getPrime(32)
            e2 = getPrime(32)
            if GCD(e1, e2) == 1:
                break
        p = getPrime(1024)
        q = getPrime(1024)
        n = p * q
        pt = sentences[random.randint(0, len(sentences) - 1)]
        message = bytes(pt, encoding=FORMAT)
        msg = bytes_to_long(message)
        ct1 = pow(msg, e1, n)
        ct2 = pow(msg, e2, n)
    print("Plaintext: ", pt)
    print("First Public exponent: ", e1)
    print("Second Public exponent: ", e2)
    print("First Modulus: ", n)
    print("First Ciphertext: ", ct1)
    print("Second Ciphertext: ", ct2)
    string = str(e1) + "." + str(e2) + "." + str(n) + "." + str(ct1) + "." + str(ct2)
    conn.send(string.encode(FORMAT))


def wiener(conn: socket) -> None:
    print("Configuring Wiener's attack")
    for _ in tqdm(range(1), desc="Configuring"):
        p = getPrime(1024)
        q = getPrime(1024)
        n = p * q
        phi = (p - 1) * (q - 1)
        while True:
            d = getPrime(256)
            e = pow(d, -1, phi)
            if e.bit_length() >= n.bit_length():
                break
        pt = sentences[random.randint(0, len(sentences) - 1)]
        message = bytes(pt, encoding=FORMAT)
        msg = bytes_to_long(message)
        ct = pow(msg, e, n)
    print("Plaintext: ", pt)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    string = str(e) + "." + str(n) + "." + str(ct)
    conn.send(string.encode(FORMAT))


def sumOPrimes(conn: socket) -> None:
    print("Configuring Sum O Primes")
    for _ in tqdm(range(1), desc="Configuring"):
        e = 65537
        p = getPrime(1024)
        q = getPrime(1024)
        n = p * q
        sum = p + q
        pt = sentences[random.randint(0, len(sentences) - 1)]
        message = bytes(pt, encoding=FORMAT)
        msg = bytes_to_long(message)
        ct = pow(msg, e, n)
    print("Plaintext: ", pt)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    string = str(e) + "." + str(n) + "." + str(ct) + "." + str(sum)
    conn.send(string.encode(FORMAT))


def configure(connection: socket, addr: str) -> None:
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
