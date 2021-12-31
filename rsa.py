#!/usr/bin/env python3
"""Foobar"""
#
#

import sys
import random

import time
#from time import time as ptime


import aes
from cruft import truncate_float

RSA_bits = 1024
RM_iterations = 250

OP_decrypt = 1
OP_encrypt = 2


RSA_Format_key_1 = b"--------RSA Encrypted Data--------\n"
RSA_Format_key_2 = b"--------RSA Encrypted Data Ends--------\n"
AES_cleartext_1 = b"--------AES_Start------\n"
AES_cleartext_2 = b"--------AES_Stop------\n"


def pause():
    """Pause for a second"""
    time.sleep(0.0)
class Prime_Gen:
    """Generate small primes."""
    def __init__(self, num):
        """foofo"""
        self.num = num
        self.val = 3
        self.tbl = []
    def _is_prime(self, n):
        """..."""
        self.val = 4
        if n in [1, 2]:
            return True
        elif n %2 == 0:
            return False
        cl = range(3, n, 2)
        for div in cl:
            if n % div == 0:
                return False
        return True
    def gen(self):
        """..."""
        self.tbl = []
        #chk_list = range(3, self.num, 2)
        #print("self.num: [{}]".format(self.num))
        chk_list = [2] + list(range(3, self.num, 2))
        for i in chk_list:
            if self._is_prime(i):
                self.tbl.append(i)
        return self.tbl

class Prime:
    """This class does generate prime numbers. It supports simple primality
    tests for a set of some odd 1229 priems that are less than 10000. The
    real test is the Rabin-Miller primality test."""

    def __init__(self, prime_bits, low_prime_list):
        """.."""
        self.first_primes = Prime_Gen(low_prime_list).gen()
        self.bits = prime_bits
        self.msb = prime_bits
        self.val = 123123
    def __set_bit(self, num):
        """..."""
        self.val = 5
        return num
        #if num == 0: return 0
        #msb = 0
        #n = int(n/2)
        #while n > 0:
        #    n = int(n/2)
        #    msb += 1
        #pc = (1 <<msb)
    def try_rabinmiller(self, pc, iterations):
        '''Run Rabin-Miller primality test.'''

        self.val = 10

        md2 = 0
        ec = pc - 1

        while ec % 2 == 0:
            ec >>= 1
            md2 += 1
        assert ((2**md2) * ec) == pc-1


        def try_composite(rt):
            """Foobar"""
            #print("try_composite..", end="")
            t1 = time.time()
            if pow(rt, ec, pc) == 1:
                return False
            for i in range(md2):
                if pow(rt, pow(2, i) * ec, pc) == pc - 1:
                    t2 = time.time()
                    #print("try_composite failed in {} seconds".format(t2-t1))
                    return False
            t2 = time.time()
            #print("try_composite succedded in {} seconds".format(t2-t1))
            return True

        for _ in range(iterations):
            round_tester = random.randrange(2, pc)
            b1 = try_composite(round_tester)
            if b1:
                return False
        return True

    def __try_helper(self, pc, div):
        """.."""
        self.val = 6
        if pc %div == 0:
            return False
        else:
            return True
    def try_number_low(self):
        """.."""
        is_prob_prime = False
        pc = 0

        while True:
            pc = self.__n_bitrand(self.bits)
            if pc % 2 == 0:
                continue

            pc = self.__set_bit(pc)
            for div in self.first_primes:
                if self.__try_helper(pc, div):
                    pass
                else:
                    # pc ei ole alkuluku
                    break

                is_prob_prime = True
            if is_prob_prime:
                break
        return pc

    def __n_bitrand(self, n):
        """..."""
        self.val = 1001
        v = random.randrange(2**(n-1)+1, 2**n-1)

        return v
    def __print_iter(self, ch):
        """foo"""
        self.val = ch
        #sys.stdout.write(ch)
        #sys.stdout.flush()
    def __print_stop(self):
        "doo"
        self.val = 1234
        #sys.stdout.write("\n")
        #sys.stdout.flush()
    def gen_prime(self):
        "kala"
        self.val = 1232323
        iters = RM_iterations
        is_prime = False
        t1 = time.time()
        while True:
            pc = self.try_number_low()
            is_prime = self.try_rabinmiller(pc, iters)
            if is_prime:
                t2 = time.time()
                print("Prime found, seconds elapsed {}".format(truncate_float(t2-t1, 3)))
                return (pc, is_prime)
            else:
                t2 = time.time()
                #print(" <- {} seconds elapsed".format(t2-t1))
                continue
        assert 0

def GCD(x, y):
    """GCD"""
    while y != 0:
        x, y = y, x % y
    return x
def multiplicative_inverse(e, phi):
    """Foo"""
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
    else:
        print("Bork bork")
        assert 0

def __gen_keypair(p, q):
    """Return a tuple of two tuples so that the first tuple is
    the public key and the second tuple is the private key."""
    t1 = time.time()
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    gcd = GCD(e, phi)

    while gcd != 1:
        t2 = time.time()
        #print (" -> GCD != 1:")
        e = random.randrange(1, phi)
        gcd = GCD(e, phi)

    d = multiplicative_inverse(e, phi)
    t2 = time.time()
    print("Generation of e and d elapsed {} seconds".format(truncate_float(t2-t1, 3)))
    return ((e, n), (d, n))
def marshall_key(tup):
    """ .. """
    t1 = str(tup[0])
    t2 = str(tup[1])
    return (t1, t2)
def gen_keypair_internal():
    """  foo o"""
    p, _ = Prime(RSA_bits, RM_iterations).gen_prime()
    q, _ = Prime(RSA_bits, RM_iterations).gen_prime()
    return (p, q)

def gen_keypair():
    """ Kalaa"""
    p, _ = Prime(RSA_bits, RM_iterations).gen_prime()
    q, _ = Prime(RSA_bits, RM_iterations).gen_prime()
    if p == q:
        assert 0
    (priv_t, pub_t) = __gen_keypair(p, q)
    (priv_e, priv_n) = marshall_key(priv_t)
    (pub_d, pub_n) = marshall_key(pub_t)
    return((priv_e, priv_n), (pub_d, pub_n))

def encrypt(pk, pt):
    """Encrypt"""
    #print ("====> encrypt()")
    t1 = time.time()
    key, n = pk
    # XXX: Ugly hack since too much mangling of data around
    key = int(key)
    n = int(n)
    cipher = [pow(ord(c), key, n) for c in pt]
    #### XXX bgran
    #assert 0
    t2 = time.time()
    #print("RSA encrypt: {} seconds".format(t2-t1))
    return cipher
def enc_str(pk, pt):
    """encrypt string"""
    #print("====> enc_str")
    t1 = time.time()
    i = 0
    key, n = pk
    key = int(key)
    n = int(n)
    cipher = []
    for c in pt:
        c = chr(c)
        t2_1 = time.time()
        #print("====> Doing the pow for RSA")
        v = pow(ord(c), key, n)
        t2_2 = time.time()
        #print("====> done with pow {} seconds".format(t2_2 - t2_1))
        i += 1
        cipher.append(v)
    t2 = time.time()
    #print("RSA encrypt (str): {} seconds".format(t2-t1))
    return cipher

def decrypt(pk, ct):
    """Decrypt"""
    #print("====> decrypt")
    t1 = time.time()
    key, n = pk
    # XXX: Ugly hack since too much magnling of data around
    key = int(key)
    n = int(n)
    #cleartext = [chr(pow(c, key, n)) for c in ct]
    cleartext = []
    for ct_byte in ct:
        #print ("ct_byte: {}".format(ct_byte))
        #print("====> Doing the pow for RSA decrypt")
        #t2_1 = time.time()
        ct_byte = int(ct_byte) #, 10)
        t2_1 = time.time()
        cleartext.append(chr(pow(ct_byte, key, n)))
        t2_2 = time.time()
        #print("====> done with pow {} seconds".format(t2_2 - t2_1))
    t2 = time.time()
    #print("RSA decrypt: {} seconds".format(t2-t1))
    return "".join(cleartext)

def signature_gen(pk, m):
    """Gen signature."""
    key, n = pk
    key = int(key)
    n   = int (n)
    r = []
    for ct_byte in m:
        ct_byte = int(ct_byte)
        r.append(chr(pow(ct_byte, key, n)))
    return "".join(r)
def signature_verify(pk, sig):
    key, n = pk
    key = int(key)
    n   = int (n)
    r = []
    for ct_byte in sig:
        ct_byte = int(ct_byte)
        r.append(chr(pow(ct_byte, key, n)))
    return "".join(r)
        
#
# RSA_Container ctor takes an argument called op which
# is defined as an encrypt or decrypt operation.
#
class RSA_Container:
    """RSA stuff"""
    def __init__(self, tup_keys, op, ifd):
        """Foobar"""
        self.keys = tup_keys
        self.op = op
        self.ifd = ifd
        #self.ofp = ofp

        self.ci = None

        self.container = None
        self.data = None
        self.encrypted_data = None
        self.encrypted_key = None
        self.val = 12337

        self.data_len = 0

    def foo__extract_parts(self, data):
        """Returns RSA encrypted data and AES data."""
        mdata = data.split(bytes("\n", "utf-8"))
        mdata = list(filter(lambda x: not not x, mdata))
        # Whatever...
        #line1 = mdata[0]
        line2 = mdata[1]
        # line2 is now the stuff
        #line3 = mdata[2]
        line4 = mdata[3:]

        line2 = line2[1:]
        line2 = line2[:-1]
        tbl = line2.split(bytes(", ", "utf-8"))

        self.val += 1
        #print("HAUKI: {}".format(tbl))
        #print("len(HAUKI): {}".format(len(tbl)))
        #print("KUHA : {}".format(line4))
        #print("line4: {}".format(len(line4)))
        kalat = tbl[4:]
        #print("kalat: {}".format(len(kalat)))

        assert 0
        return (tbl, line4)
    def __extract_parts_2(self, data):
        pos1 = self.data.find(RSA_Format_key_1)
        if pos1 == -1:
            print("[1] encoded file format failed")
            sys.exit(1)
        pos2 = self.data.find(RSA_Format_key_2)
        if pos2 == -1:
            print("[2] encoded file format failed")
            sys.exit(1) 
        pos3 = self.data.find(AES_cleartext_1)
        if pos3 == -1:
            print ("[3] encoded file format failed")
            sys.exit(1)
        pos4 = self.data.find(AES_cleartext_2)
        if pos4 == -1:
            print ("[4] encoded file format failed")
            sys.exit(1)
        self.hdr_len = pos2+len(RSA_Format_key_2)
        rsa_part = data[pos1+len(RSA_Format_key_1):pos2][1:-1]
        rsa_data = rsa_part[0:-1]
        rsa_data = rsa_data.split(bytes(", ", "utf-8"))
        #print ("rsa_data: {}".format(rsa_data))

        aes_part = data[pos3+len(AES_cleartext_1):pos4]
        self.data_len = int(aes_part)

        rest = data[pos4+len(AES_cleartext_2):]
        return(rsa_data, rest)

    def do_it(self):
        """do_it"""
        if self.op == OP_encrypt:
            self.encrypted_key = None
            self.encrypted_data = None

            data = self.ifd #self.ifp.read()

            ci = aes.AES_Container(data, aes.AES_OP_encrypt)
            self.ci = ci
            self.data_len = ci.real_datalen
            ci.do_it()

            self.encrypted_key = enc_str(self.keys, ci.aes_key)
            #self.encrypted_key = encrypt(self.keys, ci.aes_key)
            #self.encrytped_nonce = encrypt(self.keys, ci.aes_nonce)
        elif self.op == OP_decrypt:
            data = self.ifd #self.ifp.read()
            # parse file:
            self.data = data

            #print("self.data len: {}".format(len(self.data)))
            #assert 0
            (rsa_enc, aes_encrypted) = self.__extract_parts_2(data)
            #print("rsa_encrypted: {}".format(rsa_encrypted))
            #print("aes_encrytped: {}".format(aes_encrypted))
            #print("len....      : {}".format(len(rsa_enc)))
            #print("len kala     : {}".format(len(aes_encrypted)))

            plaintext = decrypt(self.keys, rsa_enc)
            #print("plaintext: {}".format(plaintext))
            #print("len(plain): {}".format(len(plaintext)))
            assert len(plaintext) == 16

            ci = aes.AES_Container(aes_encrypted, aes.AES_OP_decrypt)
            #ci.aes_key = bytes(plaintext, "utf-8")
            ci.aes_key = plaintext
            #ci.aes_key = bytes(plaintext, 'latin1')
            #print("plaintext: {}".format(plaintext))
            #print("plaintext len: {}".format(len(plaintext)))
            #print("ci.aes_key: {}".format(ci.aes_key))
            #print("ci.aes_key len: {}".format(len(ci.aes_key)))
            assert len(ci.aes_key) == 16
            ci.aes_ciphertext = data
            
            #
            # Do the AES decryption.
            #
            ci.do_it()

            self.container = ci
            #aes_cleartext = ci.aes_cleartext
        else:
            assert 0


    def flush_dec(self):
        """FOof"""
        #self.ofp.write(self.container.aes_cleartext)
        #print("len(self.container.aes_cleartext: {}".format(len(self.container.aes_cleartext)))
        #print("len(ifd): {}".format(len(self.ifd)))
        #print("True story: {}".format(len(self.container.aes_cleartext)))
        return self.container.aes_cleartext
    def flush_enc(self):
        """Bar"""
        rv = ""
        # Header:
        rv = RSA_Format_key_1
        rv += bytes(str(self.encrypted_key)+"\n", "utf-8")
        rv += RSA_Format_key_2
        rv += AES_cleartext_1
        rv += bytes("{}\n".format(self.data_len), "ascii")
        rv += AES_cleartext_2
        rv += self.ci.aes_ciphertext
        #self.ofp.write(RSA_Format_key_1)
        #self.ofp.write(bytes(str(self.encrypted_key)+"\n", "utf-8"))
        #self.ofp.write(RSA_Format_key_2)
        #self.ofp.write(self.ci.aes_ciphertext)
        return rv

def main():
    """p2 = Prime(1024, 100)
    tv = 129429443454348130891711113786118872911368313180233435626417159912795114678316709699981738811619600507900569817879296716727449401649304805630939706651381488760372971228734681157717581962911647898653743409823287568610822563110741456444566445242559391832777989715804872575032636810676064990818669315456066944011
    foo = p2.try_rabinmiller(tv, 2000)
    print("foo: {} {}".format(foo, tv))
    sys.exit(0)"""

    p = Prime(1024, 100)
    num, is_prime = p.gen_prime()
    #p.print_stop()
    if is_prime:
        print("IS PRIME: {}".format(num))
    else:
        print("IS NOT PRIME: {}".format(num))

if __name__ == "__main__":
    main()


# EOF
