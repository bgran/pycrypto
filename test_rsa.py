import unittest

import rsa, gen_rsa

class TestRSA(unittest.TestCase):
    def test_prime(self):
        return 0
        print ("====> test_prime")
        prime = rsa.Prime(rsa.RSA_bits, rsa.RM_iterations)
        num, is_prime = prime.gen_prime()
        self.assertTrue(is_prime)
    def test_enc_dec_low(self):
        #p1 = rsa.Prime(1024, 200)
        #p,_ = p1.gen_prime()
        #p2 = rsa.Prime(1024, 200)
        #q,_ = p2.gen_prime()
        print("====> test_enc_dec_low")
        self.assertTrue(gen_rsa.crypto_test())

    #def test_enc_dec_high(self):
    #    p1 = rsa.Prime(2048, 1000)
    #    p,_ = p1.gen_prime()
    #    p2 = rsa.Prime(2048, 1000)
    #    q,_ = p2.gen_prime()
    #    if gen_rsa.test(p, q):
    #        return True
    #    else:
    #        return False

    def test_primegen(self):
        print("====> test_primegen")
        primes = rsa.Prime_Gen(10000).gen()
        #print ("primes: {}".format(len(primes)))
        self.assertTrue(len(primes) == 1229)

    def test_rabinmiller(self):
        print("====> test_rabinmiller")
        ##primes = rsa.Prime_Gen(10000).gen()
        ##prime = rsa.Prime(rsa.RSA_bits, rsa.RM_iterations)
        ##p = prime.gen_prime()


if __name__ == "__main__":
    unittest.main()

