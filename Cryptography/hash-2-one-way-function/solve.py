
flags = open("flags.txt", "r").read().splitlines()
real_hash = "32333934"

# copy the hash function
def my_hash(string):
	sum = 0
	for char in string:
		sum += ord(char)
	sum = sum % 2**24
	return str(sum).encode().hex()

for flag in flags:
	hashed = my_hash(flag)
	if hashed == real_hash:
		print(flag)