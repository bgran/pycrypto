#!/usr/bin/env python3

import sys

#if __name__ != "__main__":
#	print("Usage: {} encrypted cleartext".format(sys.argv[0]))
#	sys.exit(1)
#if len(sys.argv) != 3:
#	print("Usage: {} encrypted cleartext".format(sys.argv[0]))
#	sys.exit(1)

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def __decrypt(infile, outfile, key):
	nonce, tag, ciphertext = [ infile.read(x) for x in (16, 16, -1) ]
	cipher = AES.new(key, AES.MODE_EAX, nonce)
	data = cipher.decrypt_and_verify(ciphertext, tag)
	outfile.write(data)
	return True

def __encrypt(infile, outfile, key):
	data = infile.read()
	print(type(key))
	cipher = AES.new(key, AES.MODE_EAX)
	ciphertext, tag = cipher.encrypt_and_digest(data)
	[ outfile.write(x) for x in (cipher.nonce, tag, ciphertext) ]
	return True


def aes_decrypt(infile, outfile, key):
	key = bytes(key, "ascii")
	if infile == "-":
		ifile = sys.stdin
	else:
		ifile = open(infile, "rb")
	if outfile == "-":
		ofile = sys.stdout
	else:
		ofile = open(outfile, "wb")

	if __decrypt(ifile, ofile, key):
		pass
	else:
		print("Something went wrong")
		sys.exit(1)
	return True

def aes_encrypt(infile, outfile, key):
	key = bytes(key, "ascii")
	if infile == "-":
		ifile = sys.stdin
	else:
		ifile = open(infile, "rb")
	if outfile == "-":
		ofile = sys.stdout
	else:
		ofile = open(outfile, "wb")

	if __encrypt(ifile, ofile, key):
		pass
	else:
		print("Something went wrong")
		sys.exit(1)

def gen_key():
	return get_random_bytes(16)

# EOF
