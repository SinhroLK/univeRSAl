from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
FORMAT = 'utf-8'
print("Configuring Small E attack")
e = 3
p = getPrime(1024)
q = getPrime(1024)
n = p * q
msg = bytes("Programski jezici", encoding=FORMAT)
pt = bytes_to_long(msg)
ct = pow(pt, e, n)
print(e)
print(n)
print(ct)
