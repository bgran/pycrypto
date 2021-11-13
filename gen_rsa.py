#!/usr/bin/env python3


import sys, os

import rsa, cruft

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

def crypto_test():
	print("Generating first prime")
	p1 = rsa.Prime(1024, 1000)
	p,_ = p1.gen_prime()
	print("Generating second prime")
	p2 = rsa.Prime(1024, 1000)
	q,_ = p2.gen_prime()

	test(p, q)


def main():
	
	#print("Enter PYCRYPTO filename: ",end="")
	defa = os.path.join(cruft.get_key_dir(), "key")
	#foo = "avain"
	foo = input("Enter key file name (default is {})> ".format(defa))
	if foo == "":
		assert(0)
	data = None
	#if foo == "avain":
	#	os.unlink("avain")#
	#	os.unlink("avain.pub")
	try:
		data = os.stat(foo)
	except FileNotFoundError:
		pass
	else:
		print("File exists, exiting..")
		sys.exit(1)
	try:
		data = os.stat(foo+".pub")
	except FileNotFoundError:
		pass
	else:
		print("File .pub exists, exiting..")
		sys.exit(1)

	filef_priv = open(foo, "wb")
	filef_pub  = open(foo+".pub", "wb")

	priv, pub = rsa.gen_keypair()
	print("priv: {}".format(priv))
	print("pub:  {}".format(pub))

	priv_comb = priv[0] + "\n" + priv[1]
	pub_comb = pub[0] + "\n" + pub[1]

	priv_bytes = str.encode(priv_comb)
	pub_bytes = str.encode(pub_comb)

	filef_priv.write(priv_bytes)
	filef_pub.write(pub_bytes)
	filef_priv.close()
	filef_pub.close()
	print ("Wrote keys..")
	sys.exit(0)

	outf = None
	inf = None
	infile = None
	outfile = None
	argv = sys.argv[1:]
	opts, arg = None, None
	try:
		opts, args = getopt.getopt(argv, "o:i:")
	except:
		print("Bork bork")
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
	
	


	
	crypto_test()

	

if __name__ == "__main__":
	main()


# EOF
