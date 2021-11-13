#!/usr/bin/env python3


import sys

import rsa

def usage():
	print ("Usage: {} -i inputfile -o outputfile".format(sys.argv[0]))
	print ("Will output a RSA keypair to $HOME/.pycrypto..")

def test(p, q):
	cleartext = "hello world"
	#print("test with {}".format(cleartext))
	((e,n), (d,m)) = rsa.gen_keypair(p, q)

	#print("encrypting: {}".format(cleartext))
	ct = rsa.encrypt((e,n), cleartext)
	#print("decrypting: {}".format(ct))
	r  = rsa.decrypt((d, m), ct)
	#print("kala on siis: {}".format(r))
	if cleartext == r:
		return True
	else:
		return False

def main():
	outf = None
	inf = None
	infile = None
	outfile = None
	argv = sys.argv[1:]
	try:
		opts, args = getopt.getopt(argv, "o:i:")
	except:
		print ("Error")
		usage()
		sys.exit(1)
	for opt, arg in opts:
		if opt in ["-o"]:
			outfile = arg
		elif opt in ["-i"]:
			infile = arg
	if (outfile == "-"):
		outf = sys.stdout
	else:
		outf = open(outfile, "bw")
	if (infile == "-"):
		inf = sys.stdin
	else:
		inf = open(infile, "br")
	
	cleartext 
			

	if len(sys.argv) > 1:
		usage()
		sys.exit(1)
	print("Generating first prime")
	p1 = rsa.Prime(1024, 1000)
	p,_ = p1.gen_prime()
	print("Generating second prime")
	p2 = rsa.Prime(1024, 1000)
	q,_ = p2.gen_prime()

	test(p, q)

	

if __name__ == "__main__":
	main()


# EOF
