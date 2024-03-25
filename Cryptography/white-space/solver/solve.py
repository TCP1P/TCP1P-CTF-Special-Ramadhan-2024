f = open("output.txt", "r")
flag = f.read().split("\n")

key_1 = 0
key_2 = 0

for data in range(1, 65):
    if(chr(len(flag[0]) // data) == "T"):
        key_1 = data
        break

for data in range(1, 65):
    if(chr(len(flag[1]) // data) == "C"):
        key_2 = data
        break

plain = ""
for i, data in enumerate(flag):
    if(i % 2 == 0):
        plain += chr(len(data) // key_1)
    if(i % 2 == 1):
        plain += chr(len(data) // key_2)

print(plain)