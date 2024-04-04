from ctypes import CDLL

# get srand and rand from libc

libc = CDLL("/usr/lib/libc.so.6")

flag_enc_file = open("flag_enc.txt", "rb").read().strip()

seed = int.from_bytes(flag_enc_file[:4], "little")
flag_enc = flag_enc_file[4:]
libc.srand(seed)

flag = ""

for c in flag_enc:
    key = libc.rand() & 0xFF
    libc.rand()
    flag += chr(c ^ (key))

print(f"Random seed: {seed}")
print(f"Flag: {flag}")
