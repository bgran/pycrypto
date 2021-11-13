#
#
#

import sys,os

def get_key_dir():
	rv = ""
	env = os.environ
	if not env.has_key("PYCRYPTO_KEYS"):	
	else:
		hd = env.has_key("HOME")
		if not hd:
			print("This is unaccetable")
			sys.exit(1)
		rv = os.path.join(hd, ".pycrypto")
		if os.path.exists(rv): return rv
		else: os.mkdir(rv)
	return rv

def get_keypair():
	env = os.environ
	fd = None
	if not env.has_key("PYCRYPTO_KEYS"):
		print("Set PYCRYPTO_KEYS to continue")
		sys.exit(1)
	try:
		fd = open(env["PYCRYPTO_KEYS"], "r")
	except IOError, e:
		print ("Couldn't open {} for reading".format(env["PYCRYPTO_KEYS"))
		sys.exit(1)
	data = fd.read()

def read_priv_key():
	d = None
	path = get_key_dir()
	rfile = os.path.join(path, "key")
	with open(rfile, "rb") as f:
		d = f.read()
	(e, n) = d.split("\n")
	return (e, n)
def read_pub_key():
	d = None
	path = get_key_dir()
	rfile = os.path.join(path, "key.pub")
	with open(rfile, "rb") as f:
		d = f.read()
	(d, n) = d.split("\n")
	return (d, n)



# EOF
