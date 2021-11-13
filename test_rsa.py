import unittest

import rsa, gen_rsa

class TestRSA(unittest.TestCase):
	def test_prime(self):
		prime = rsa.Prime(1024, 200)
		num, is_prime = prime.gen_prime()
		self.assertTrue(is_prime)
	def test_enc_dec_low(self):
		p1 = rsa.Prime(1024, 200)
		p,_ = p1.gen_prime()
		p2 = rsa.Prime(1024, 200)
		q,_ = p2.gen_prime()
		self.assertTrue(gen_rsa.test(p, q))

	#def test_enc_dec_high(self):
	#	p1 = rsa.Prime(2048, 1000)
	#	p,_ = p1.gen_prime()
	#	p2 = rsa.Prime(2048, 1000)
	#	q,_ = p2.gen_prime()
	#	if gen_rsa.test(p, q):
	#		return True
	#	else:
	#		return False

	def test_primegen(self):
		primes = rsa.Prime_Gen(10000).gen()
		print ("primes: {}".format(len(primes)))
		self.assertTrue(len(primes) == 1229)


if __name__ == "__main__":
	unittest.main()

