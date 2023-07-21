import owiener
import threading
import socket
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot, root
from maths import chinese_remainder_theorem
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


def smallE(known):
    print("***************************************************************************************")
    e = int(known.split(".")[0])
    n = int(known.split(".")[1])
    ct = int(known.split(".")[2])
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    print("Plaintext: ", long_to_bytes(iroot(ct, e)[0]).decode(FORMAT))


def hastad(known):
    print("***************************************************************************************")
    splitList = known.split(".")
    e = int(splitList[0])
    n = []
    ct = []
    for i in range(1, len(splitList) - 1):
        if i % 2 != 0:
            n.append(int(splitList[i]))
        else:
            ct.append(int(splitList[i]))
    print("Public exponent: ", e)
    print("Modulus: ", n)
    print("Ciphertext: ", ct)
    """for i, j, k in combinations(range(e), 3):
        C = chinese_remainder_theorem([(ct[i], n[i]), (ct[j], n[j]), (ct[k], n[k])])
        try:
            M = int(root(C, 3))
        except ValueError:
            pass
        else:
            print(long_to_bytes(M))"""

    chineseList = []
    for i in range(e):
        chineseList.append((ct[i], n[i]))
    C = chinese_remainder_theorem(chineseList)
    try:
        M = int(root(C, e))
    except ValueError:
        pass
    print(long_to_bytes(M).decode(FORMAT))


def wiener(known):
    print("***************************************************************************************")
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


def solver():

    while True:
        rec = clientSocket.recv(HEADER).decode(FORMAT)
        if int(rec.split(".")[0]) == 3:
            smallE(rec)
        elif 3 < int(rec.split(".")[0]) <= 20:
            hastad(rec)
        elif int(rec.split(".")[0]).bit_length() == int(rec.split(".")[1]).bit_length():
            wiener(rec)


try:
    receive_thread = threading.Thread(target=solver)
    receive_thread.start()
except:
    print("Client closed")
