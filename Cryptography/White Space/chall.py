import random
from secret import flag

def enc(flag):
    c = ""
    key_1 = random.randint(0, 64)
    key_2 = random.randint(0, 64)
    for i, chr in enumerate(flag):
        if (i % 2 == 0):
            c += (" " * (ord(chr) * key_1)) + "\n"
        if (i % 2 == 1):
            c += (" " * (ord(chr) * key_2)) + "\n"
    return c

def file(cipher):
    file = open("output.txt", "w")
    file.write(cipher)
    file.close()

cipher = enc(flag)
file(cipher)