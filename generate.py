#! /bin/python

# check if the command is correctly called
from sys import argv
if len(argv) != 3:
	print("Usage: generate <n> <length>")
	exit(1)
try:
	n , l = int(argv[1]) , int(argv[2])
except:
        print("Usage: generate <n> <length>")
        exit(1)
if not (n>0 and l>0):
	print("Both <n> and <length> should be positive integers.")
	exit(1)
del argv

# generate and import random bytes using openssl
L = round(n * l * (256/(126-33+1)) * 50)
from subprocess import check_output
try:
	# check wehter openssl is installed or not
	b64_bytes = check_output([f"openssl rand -base64 {L}"] , shell=True)
except:
	print("Please install OpenSSL module first")
	exit(2)
del check_output

# decode base64 bytes
from base64 import b64decode
bytes = b64decode(b64_bytes)
del b64decode

# filter bytes and convert it to string
string = ''
for byte in bytes:
	if 33 <=int(byte) <= 126:
		string += chr(byte)

# generate header and footer
if l <= 42:
	header = 12*"-" + "BEGIN PASSWORD SET" + 12*"-"
	footer = 13*"-" + "END PASSWORD SET" + 13*"-"
else:
	h = (l-18) // 2
	header = h*"-" + "BEGIN PASSWORD SET" + (h+(l%2))*"-"
	footer = (h+1)*"-" + "END PASSWORD SET" + (h+1+(l%2))*"-"

# print the output
print()
print(header)
for k in range(1,n+1):
	print(string[k*l-l:k*l])
print(footer)

exit(0)
