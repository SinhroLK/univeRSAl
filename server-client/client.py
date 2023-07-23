import owiener
import threading
import socket
from Crypto.Util.number import GCD, long_to_bytes
from gmpy2 import iroot, invert
from factordb.factordb import FactorDB

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


###########################################################################
def crt(ct: list, m: list) -> int:
    try:
        assert len(ct) == len(m)
    except:
        print("[+] Length of ct should be equal to length of m")
        return -1
    for i in range(len(m)):
        for j in range(len(m)):
            if GCD(m[i], m[j]) != 1 and i != j:
                print("[+] Input not pairwise co-prime")
                return -1

    M = 1
    for i in m:
        M *= i
    list_b = [M//i for i in m]
    assert len(list_b) == len(m)
    try:
        list_b_inv = [int(invert(list_b[i], m[i])) for i in range(len(m))]
    except:
        print("[+] Encountered an unusual error while calculating inverse using gmpy2.invert()")
        return -1
    x = 0
    for i in range(len(m)):
        x += ct[i]*list_b[i]*list_b_inv[i]
    return x % M


def hastad_unpadded(ct_list: list, mod_list: list, e: int) -> bytes:
    m_expo = crt(ct_list, mod_list)
    if m_expo != -1:
        eth_root = iroot(m_expo, e)
        if not eth_root[1]:
            return b"[+] Cannot calculate eth root!"
        elif eth_root[1]:
            return long_to_bytes(eth_root[0])
    else:
        return b"[+] Cannot calculate CRT"
#########################################################################


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

    print(hastad_unpadded(ct, n, e))


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
        f = FactorDB(n)
        f.connect()
        p = f.get_factor_list()[0]
        print(p)
        print(n)


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


def solver():
    while True:
        rec = clientSocket.recv(HEADER).decode(FORMAT)
        if int(rec.split(".")[0]) == 3:
            smallE(rec)
        elif 3 < int(rec.split(".")[0]) <= 20:
            hastad(rec)
        elif int(rec.split(".")[0]).bit_length() == int(rec.split(".")[1]).bit_length():
            wiener(rec)
        elif len(rec.split(".")) == 4:
            sumOPrimes(rec)


try:
    receive_thread = threading.Thread(target=solver)
    receive_thread.start()
except:
    print("Client closed")
