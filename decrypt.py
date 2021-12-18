#!/usr/bin/env python3

if __name__ != "__main__":
    import sys
    print("This is a program, not a module")
    sys.exit(1)
    

import cruft
import sys
import getopt
import codecs

import rsa
import aes

def usage():
    print("Usage: {} -i inputfile -o outputfile -c private_key_file".format(sys.argv[0]))
    print("        -i    File to decrypt")
    print("        -o    File to store encrytion result")
    print("        -c    File containing secret key")
    print("        -h    This message")

def main():
    cfile = None
    ofile = None
    ifile = None
    cfp = None
    ofp = None
    ifp = None
    opts, arg = None, None
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "ho:i:c:")
    except:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ["-o"]:
            ofile = arg
        elif opt in ["-i"]:
            ifile = arg
        elif opt in ["-c"]:
            cfile = arg
        elif opt in ["-h"]:    
            usage()
            sys.exit(0)

    if not ofile:
        assert 0

    #if (ofile == "-" or ifile is None):
    #    ofp = sys.stdout
    #    print("we don't support yet writing to stdout")
    #    usage()
    #    sys.exit(1)
    #else:
    #    ofp = open(ofile, "wb")

    #if (ifile == "-" or ifile is None):
    #    ifp = sys.stdin
    #    print("We don't support yet reading from stdin")
    #    usage()
    #    sys.exit(1)
    #else:
    #    ifp = open (ifile, "rb")

    ifd = ""
    with open(ifile, "rb") as input_file:
            ifd = input_file.read()
    #print("ifd: {}".format(ifd))
    #assert 0
    if not cfile:
        print("cfile undefined")
        sys.exit(1)
        
    d, n = cruft.read_priv_key(cfile)

    #
    # Do RSA and AES processing
    #
    rsa_container = rsa.RSA_Container((d, n), rsa.OP_decrypt, ifd)
    rsa_container.do_it()
    clear_text = rsa_container.flush_dec()


    print("clear_text: {}".format(len(clear_text)))
    print("data_len:   {}".format(rsa_container.data_len))
    

    #
    # Split clear_text to fit the stuff
    #
    #clear_text = clear_text[rsa_container.hdr_len:]
    clear_text = clear_text[:rsa_container.data_len]



    #
    # Write output to file
    #
    with open(ofile, "wb") as output_file:
        print ("openinig shit")
        output_file.write(clear_text)
if __name__ == "__main__":
    main()

# EOF
