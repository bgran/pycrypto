#!/usr/bin/env python3
#
#

import sys
import random

import time
from time import time as ptime

RM_iterations = 20

def pause():
	time.sleep(0.0)
class Prime_Gen:
	"""Generate small primes."""
	def __init__(self, num):
		self.num = num
	def __is_prime(self, n):
		if n == 1: return True
		elif n == 2: return True
		elif n %2 == 0:
			return False
		cl = range(3, n, 2)
		for div in cl:
			if n % div == 0:
				return False
		return True
	def gen(self):
		self.tbl = []
		#chk_list = range(3, self.num, 2)
		chk_list = [2] + list(range(3, self.num, 2))
		for i in chk_list:
			if self.__is_prime(i):
				self.tbl.append(i)
		return(self.tbl)

class Prime:
	def __init__(self, prime_bits, low_prime_list):
		self.first_primes= Prime_Gen(low_prime_list).gen()
		#print(list(self.first_primes))
		self.bits = prime_bits
	def try_rabinmiller(self, pc, iterations):
		'''Run Rabin-Miller primality test.'''
		#print("Entering with pc: {} iterations: {}".format(pc, iterations))
		pause()
		md2 = 0
		ec = pc - 1
		t1 = ptime()

		#print("ec: {}".format(ec))
		while ec % 2 == 0:
			#print ("RM: ec: {}".format(ec))
			ec >>= 1
			md2 += 1
		assert(((2**md2) * ec) == pc-1) 
		#print("ec after: {}".format(ec))


		pi = 100

		def try_composite(rt):
			#print("try_composite(): {}".format(rt))
			if pow(rt, ec, pc) == 1:
				return False
			for i in range(md2):
				#if pow(rt, 2**i * ec, pc) == pc - 1:
				if pow(rt, pow(2, i) * ec, pc) == pc - 1:
					return False
			return True

		for i in range(iterations):
			round_tester = random.randrange(2,
				pc)
			b1 = try_composite(round_tester)
			pi -= 1
			if pi == 0:
				pi = 100
				self.print_iter("*")
			if b1: 
				return False
		t2 = ptime()
		#print("Rabin-Miller (True) lasted: {} seconds".format(t2-t1))
		return True
		
	def __try_helper(self, pc, div):
		if pc %div == 0:
			#print("{} / {} pc % div on nolla eli pc ei ole alkuluku".format(pc, div))
			return False
		else:
			#print("pc voi olla alkuluku")
			return True
	def try_number_low(self):
		is_prob_prime = False
		pc = 0

		pi = 100
		while True:
			#pi -= 1
			#if pi == 0:
			#	self.print_iter(".")
			#	pi = 100

			pc = self.__n_bitrand(self.bits)
			if pc % 2 == 0:
				continue
			#print("pc: {}".format(pc))
			for div in self.first_primes:

				pi -= 1
				if pi == 0:
					self.print_iter(".")
					pi = 100

				#print("div: {}".format(div))

				if self.__try_helper(pc, div):
					pass
				else:
					# pc ei ole alkuluku
					break
					
				is_prob_prime = True
			if is_prob_prime: break
		return pc
		
	def __n_bitrand(self, n):
		v = random.randrange(2**(n-1)+1, 2**n-1)
		return v
	def __print_iter(self, ch):
		return
		sys.stdout.write(ch)
		sys.stdout.flush()
	def __print_stop(self):
		return
		sys.stdout.write("\n")
		sys.stdout.flush()
	def gen_prime(self):
		iters = RM_iterations
		is_prime = False
		while True:
			pc = self.try_number_low()
			is_prime = self.try_rabinmiller(pc, iters)
			if is_prime:
				return (pc, is_prime)
			else:
				continue
		assert 0
	

class RSA_key:
	def __init__(self):
		pass

	def __get_prime(self, bits):
		pass		

	def _ctor(self, bits):
		prime1 = self.__gen_prime(bits)


def GCD(x, y):
	while y != 0:
		x, y = y, x % y
	return x
def multiplicative_inverse(e, phi):
	d = 0
	x1 = 0
	x2 = 1
	y1 = 1
	temp_phi = phi
	while e > 0:
		temp1 = int(temp_phi/e)
		temp2 = temp_phi - temp1 * e
		temp_phi = e
		e = temp2

		x = x2 - temp1 * x1
		y = d - temp1 * y1
	
		x2 = x1
		x1 = x
		d = y1
		y1 = y
	if temp_phi == 1:
		return d + phi


def gen_keypair(p, q):
	#print("type: p: {}".format(type(p)))
	#print("type: q: {}".format(type(q)))
	n = p * q
	phi = (p-1) * (q-1)
	e = random.randrange(1, phi)
	gcd = GCD(e, phi)

	while gcd != 1:
		e = random.randrange(1, phi)
		gcd = GCD(e, phi)
	
	#e = float(e)
	#phi = float(phi)
	d = multiplicative_inverse(e, phi)
	return ((e, n), (d, n))

def encrypt(pk, pt):
	key, n = pk
	#print("KALAA: {}".format(type(pt)))
	#print("pt koko: {}".format(len(pt)))
	#print("key koko: {}".format(key))
	#cipher = [(ord(c) ** key) % n for c in pt]
	#cipher = int(pow(ord(c), key, n
	cipher = [pow(ord(c), key, n) for c in pt]
	return cipher

def decrypt(pk, ct):
	key, n = pk
	#cleartext = [chr((c ** key) % n) for c in ct]
	cleartext = [chr(pow(c, key, n)) for c in ct]
	return "".join(cleartext)

def main():
	"""p2 = Prime(1024, 100)
	tv = 129429443454348130891711113786118872911368313180233435626417159912795114678316709699981738811619600507900569817879296716727449401649304805630939706651381488760372971228734681157717581962911647898653743409823287568610822563110741456444566445242559391832777989715804872575032636810676064990818669315456066944011
	foo = p2.try_rabinmiller(tv, 2000)
	print("foo: {} {}".format(foo, tv))
	sys.exit(0)"""
	
	p = Prime(1024, 100)
	num, is_prime = p.gen_prime()
	p.print_stop()
	if is_prime:
		print("IS PRIME: {}".format(num))
	else:
		print("IS NOT PRIME: {}".format(num))

if __name__ == "__main__":
	main()


# EOF
