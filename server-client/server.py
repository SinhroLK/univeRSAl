import socket
import threading
import random
from Crypto.Util.number import bytes_to_long, getPrime, GCD
from tqdm import tqdm
from sentences import sentences

# server configuration
FORMAT = 'utf-8'
HEADER = 100000
serverPort = 5061
serverName = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen()


def smallE(conn: socket) -> None:
    print("Configuring Small e attack")
    e = 3
    # generating small e attack data
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
    # sending data to the client
    string = str(e) + "." + str(n) + "." + str(ct)
    conn.send(string.encode(FORMAT))


def hastad(conn: socket) -> None:
    print("Configuring Hastad's attack")
    # generating e from a list of prime numbers
    eList = [2, 3, 5, 7, 11, 13, 17, 19]
    e = eList[random.randint(0, len(eList) - 1)]
    # selecting a sentence to encrypt
    pt = sentences[random.randint(0, len(sentences) - 1)]
    n = []
    ct = []
    message = bytes(pt, encoding=FORMAT)
    # generating e different n, and calculating ct for every n
    for i in tqdm(range(e), desc="Configuring"):
        p = getPrime(1024)
        q = getPrime(1024)
        n.append(p * q)
        ct.append(pow(bytes_to_long(message), e, n[i]))
    print("Plaintext: ", pt)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    # sending data to the client
    string = str(e) + "."
    for i in range(e):
        string = string + str(n[i]) + "." + str(ct[i]) + "."
    conn.send(string.encode(FORMAT))


def commonModulus(conn: socket) -> None:
    # configuring data for common modulus attack
    # we need to public expoents, one modulus and one message to encrypt. By calculating everything we get to cts
    print("Configuring Common modulus")
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
    # sending data to the client
    string = str(e1) + "." + str(e2) + "." + str(n) + "." + str(ct1) + "." + str(ct2)
    conn.send(string.encode(FORMAT))


def wiener(conn: socket) -> None:
    print("Configuring Wiener's attack")
    # generating data for Wiener's attack
    for _ in tqdm(range(1), desc="Configuring"):
        p = getPrime(1024)
        q = getPrime(1024)
        n = p * q
        phi = (p - 1) * (q - 1)
        while True:
            d = getPrime(256)
            e = pow(d, -1, phi)  # calculating e as a modular inverse of d using Euler's totient
            if e.bit_length() == n.bit_length():
                break
        pt = sentences[random.randint(0, len(sentences) - 1)]
        message = bytes(pt, encoding=FORMAT)
        msg = bytes_to_long(message)
        ct = pow(msg, e, n)
    print("Plaintext: ", pt)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    # sending data to the client
    string = str(e) + "." + str(n) + "." + str(ct)
    conn.send(string.encode(FORMAT))


def sumOPrimes(conn: socket) -> None:
    print("Configuring Sum O Primes")
    # generating data for SumOPrimes
    for _ in tqdm(range(1), desc="Configuring"):
        e = 65537
        p = getPrime(1024)
        q = getPrime(1024)
        n = p * q
        sum = p + q #calculating the sum of factors
        pt = sentences[random.randint(0, len(sentences) - 1)]
        message = bytes(pt, encoding=FORMAT)
        msg = bytes_to_long(message)
        ct = pow(msg, e, n)
    print("Plaintext: ", pt)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    # sending data to the client
    string = str(e) + "." + str(n) + "." + str(ct) + "." + str(sum)
    conn.send(string.encode(FORMAT))


def configure(connection: socket, addr: str) -> None:
    print(f'New connection at {addr}')
    print(r"""                                          
                           ███                       ███████████    █████████    █████████   ████ 
                           ░░░                       ░░███░░░░░███  ███░░░░░███  ███░░░░░███ ░░███ 
     █████ ████ ████████   ████  █████ █████  ██████  ░███    ░███ ░███    ░░░  ░███    ░███  ░███ 
    ░░███ ░███ ░░███░░███ ░░███ ░░███ ░░███  ███░░███ ░██████████  ░░█████████  ░███████████  ░███ 
     ░███ ░███  ░███ ░███  ░███  ░███  ░███ ░███████  ░███░░░░░███  ░░░░░░░░███ ░███░░░░░███  ░███ 
     ░███ ░███  ░███ ░███  ░███  ░░███ ███  ░███░░░   ░███    ░███  ███    ░███ ░███    ░███  ░███ 
     ░░████████ ████ █████ █████  ░░█████   ░░██████  █████   █████░░█████████  █████   █████ █████
      ░░░░░░░░ ░░░░ ░░░░░ ░░░░░    ░░░░░     ░░░░░░  ░░░░░   ░░░░░  ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░ 
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
            # connecting the client to the server and starting the configure function
            connectionSocket, address = serverSocket.accept()
            thread_main = threading.Thread(target=configure, args=(connectionSocket, address,))
            thread_main.start()
        except:
            print("Server killed")
