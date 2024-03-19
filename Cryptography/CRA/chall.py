from Crypto.Util.number import *
from secret import flag

p = getStrongPrime(1024)
q = getStrongPrime(1024)
n = p * q

def enc(n, secret):
    e = 3
    plain = bytes_to_long(secret)
    cipher = pow(plain, e, n)
    return cipher

def file(cipher):
    file = open("output", "w")
    file.write(str(cipher))
    file.close

c = enc(n, flag)
file(c)