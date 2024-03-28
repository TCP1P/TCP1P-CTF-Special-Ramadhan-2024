
# copy the hash function
def my_hash(string):
	sum = 0
	for char in string:
		sum += ord(char)
	sum = sum % 2**24
	print(sum)
	return str(sum).encode().hex()


# original admin password: supersecurepassword1234
# hashed (hex): 32323931

# find a string such that the hash equals 32323931
hashed = '32323931'

print(int(bytes.fromhex(hashed).decode())) # 2291 --> "sum" value

# cari string yang jumlah ord nya 2291
# 97*22 + 78 + 79 = 2291
contoh = "aaaaaaaaaaaaaaaaaaaaaaNO"

print(contoh)
print(my_hash('aaaaaaaaaaaaaaaaaaaaaaNO'))
