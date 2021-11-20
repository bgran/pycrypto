#!/usr/bin/env python3

import sys

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

AES_OP_decrypt = 241
AES_OP_encrypt = 242

def __decrypt(infile, outfile, key):
	nonce, tag, ciphertext = [ infile.read(x) for x in (16, 16, -1) ]
	cipher = AES.new(key, AES.MODE_EAX, nonce)
	data = cipher.decrypt_and_verify(ciphertext, tag)
	outfile.write(data)
	return True

def __encrypt(infile, outfile, key):
	data = infile.read()
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
	#return get_random_bytes(16)
	rv = []
	for i in range(16):
		rv.append(ord(get_random_bytes(1)))
	return rv
def orig_gen_key():
	return get_random_bytes(16)
	


class AES_Container():
	def __init__(self, data, op):
		self.aes_key = None
		self.aes_ciphertext = None
		self.aes_cleartext = None
		self.rsa_key = None

		self.content = data
	
		if op == AES_OP_encrypt:
			length = 16 - (len(self.content) % 16)
			self.content += bytes([length])*length
		elif op == AES_OP_decrypt:
			length = 16 - (len(self.content) % 16)
			self.content += bytes([length])*length
		else:
			print("Bork bork")
			sys.exit(1)

		self.op = op
	def __c_ify_list(self, lst):
		for i in [chr(c) for c in lst]:
			print ("__c_ify_list: {}".format(i))
	def __conv_aes(self, lst):
		r = b''
		for i in lst:
			r += bytes(chr(i))
		return r
		rv = []
		for l in lst:
			rv.append(chr(l))
		return bytes("".join(rv), 'utf-8')
	def __conv_rsa(self, rv):
		return rv
	def do_it(self):
		if self.op == AES_OP_encrypt:
			# This is it, the american dream
			#
			# aes_sec is 128-bit large, the default
			# length of the AES cipher block.
			aes_sec = orig_gen_key()
			#aes_sec = self.__conv_aes(rsa_sec)
			ci = AES.new(aes_sec, AES.MODE_CBC)

			self.aes_key = aes_sec

			# 128-bits
			assert len(self.aes_key) == 16

			self.aes_ciphertext = ci.encrypt(self.content)
		elif self.op == AES_OP_decrypt:
			aes_sec = self.aes_key
			ci = AES.new(aes_sec, AES.MODE_CBC)
			#self.aes_cleartext = ci.decrypt(self.aes_ciphertext)
			self.aes_cleartext = ci.decrypt(self.content)
		else:
			assert 0

# EOF
