import owiener
import threading
import socket
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot
from factordb.factordb import FactorDB
from maths import hastad_unpadded, extended_gcd

FORMAT = 'utf-8'
HEADER = 100000
serverPort = 5060
serverName = socket.gethostbyname(socket.gethostname())
username = ''
stop = False
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print(r"""                                          
         ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
        ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
        ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌
        ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌
        ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌
        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌
        ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌
        ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌
        ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌
        ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌
         ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀        ▀▀ 
         """)


def smallE(known: str) -> None:
    print("***************************************SMALL E***************************************")
    e = int(known.split(".")[0])
    n = int(known.split(".")[1])
    ct = int(known.split(".")[2])
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    print("Plaintext: ", long_to_bytes(iroot(ct, e)[0]).decode(FORMAT))


def hastad(known: str) -> None:
    print("***************************************HASTAD***************************************")
    splitList = known.split(".")[:-1]
    e = int(splitList[0])
    n = []
    ct = []
    for i in range(1, len(splitList)):
        if i % 2 != 0:
            n.append(int(splitList[i]))
        else:
            ct.append(int(splitList[i]))
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    print("Plaintext: ", hastad_unpadded(ct, n, e).decode(FORMAT))


def wiener(known: str) -> None:
    print("***************************************WIENER***************************************")
    e = int(known.split(".")[0])
    n = int(known.split(".")[1])
    ct = int(known.split(".")[2])
    d = owiener.attack(e, n)
    if d:
        print("Public exponent: ", e)
        print("Modulus: ", n)
        print("Ciphertext: ", ct)
        print("Plaintext: ", long_to_bytes(pow(ct, d, n)).decode(FORMAT))
    else:
        print("No Luck")


def sumOPrimes(known: str) -> None:
    # sum = p + q && phi = (p-1)(q-1) = pq - p - q +1  = n - (p + q) + 1 ==> phi = n - sum + 1
    print("***************************************SumOPrimes***************************************")
    e = int(known.split(".")[0])
    n = int(known.split(".")[1])
    ct = int(known.split(".")[2])
    sum = int(known.split(".")[3])
    phi = n - sum + 1
    d = pow(e, -1, phi)
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    print("Plaintext: ", long_to_bytes(pow(ct, d, n)).decode(FORMAT))


def commonModulus(known: str) -> None:
    print("***************************************CommonModulus***************************************")
    e1 = int(known.split(".")[0])
    e2 = int(known.split(".")[1])
    n = int(known.split(".")[2])
    ct1 = int(known.split(".")[3])
    ct2 = int(known.split(".")[4])
    u, v, _ = extended_gcd(e1, e2)

    pt = pow(ct1, u, n) * pow(ct2, v, n) % n
    print("First Public exponent: ", e1)
    print("Second Public exponent: ", e2)
    print("Modulus: ", n)
    print("First Ciphertext: ", ct1)
    print("Second Ciphertext: ", ct2)
    print("Plaintext: ", long_to_bytes(pt).decode(FORMAT))


def solver() -> None:
    while True:
        rec = clientSocket.recv(HEADER).decode(FORMAT)
        if int(rec.split(".")[0]) == 3:
            smallE(rec)
        elif 3 < int(rec.split(".")[0]) <= 20:
            hastad(rec)
        elif len(rec.split(".")) == 5:
            commonModulus(rec)
        elif int(rec.split(".")[0]).bit_length() == int(rec.split(".")[1]).bit_length():
            wiener(rec)
        elif len(rec.split(".")) == 4:
            sumOPrimes(rec)



try:
    receive_thread = threading.Thread(target=solver)
    receive_thread.start()
except:
    print("Client closed")
