#
#
#

import sys,os

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

# EOF
