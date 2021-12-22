#
#
#

import sys,os
import math


def debug(s):
    sys.stderr.write(s)
    sys.stderr.flush()
def get_key_dir():
    rv = ""
    env = os.environ
    if not "PYCRYPTO_KEYS" in env:
        rv = os.path.join(env["HOME"], ".pycrypto")
        if not os.path.exists(rv):
            os.mkdir(rv)
        return rv
    else:
        hd = "HOME" in env
        if not hd:
            print("This is unaccetable")
            sys.exit(1)
        rv = os.path.join(hd, ".pycrypto")
        if os.path.exists(rv): return rv
        else: os.mkdir(rv)
    return rv

def __bork_get_keypair():
    env = os.environ
    fd = None
    if not env.has_key("PYCRYPTO_KEYS"):
        print("Set PYCRYPTO_KEYS to continue")
        sys.exit(1)
    try:
        fd = open(env["PYCRYPTO_KEYS"], "r")
    except IOError:
        print ("Couldn't open {} for reading".format(env["PYCRYPTO_KEYS"]))
        sys.exit(1)
    data = fd.read()

def read_priv_key(fn):
    d = None
    #path = get_key_dir()
    #rfile = os.path.join(path, "key")
    with open(fn, "rb") as f:
        d = bytes(f.read())
    (e, n) = d.split(bytes("\n", "utf-8"))
    e = int(e)
    n = int(n)
    return (e, n)
def read_pub_key(fn):
    d = None
    #path = get_key_dir()
    #rfile = os.path.join(path, "key.pub")
    with open(fn, "rb") as f:
        d = bytes(f.read())
    (d, n) = d.split(bytes("\n", 'utf-8'))
    d = int(d)
    n = int(n)
    return (d, n)

def truncate_float(number, digits):
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


# EOF
