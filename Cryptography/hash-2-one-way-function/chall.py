import random

flags = open("flags.txt", "r").read().splitlines()
flag = random.choice(flags)

# my totally original hash function!!!1!
def my_hash(string):
	sum = 0
	for char in string:
		sum += ord(char)
	sum = sum % 2**24
	return str(sum).encode().hex()

print(my_hash(flag)) # output: 32333934