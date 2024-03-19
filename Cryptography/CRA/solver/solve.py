from sympy import cbrt
from Crypto.Util.number import *

file = open("output.txt", "rb")
plain = cbrt(int(file.read()))
print(long_to_bytes(plain))