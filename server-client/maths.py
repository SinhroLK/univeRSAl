from Crypto.Util.number import GCD, long_to_bytes
from gmpy2 import iroot, invert


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
    list_b = [M // i for i in m]
    assert len(list_b) == len(m)
    try:
        list_b_inv = [int(invert(list_b[i], m[i])) for i in range(len(m))]
    except:
        print("[+] Encountered an unusual error while calculating inverse using gmpy2.invert()")
        return -1
    x = 0
    for i in range(len(m)):
        x += ct[i] * list_b[i] * list_b_inv[i]
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



def extended_gcd(a, b):
    if a % b:
        u, v, d = extended_gcd(b, a % b)
        return v, (d - a * v) // b, d

    return 0, 1, b