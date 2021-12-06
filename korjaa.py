#!/usr/bin/env python3
import sys
d = open(sys.argv[1]).readlines()
largerv = []

def only_spaces(s):
	state = 0
	for c in s:
		if c == "\n":
			break
		if c != " ":
			state = 1
	return state
def rev(lne):
	return lne[::-1]
def trailing_whitespace(line):
	rv = False
	l = line
	l = rev(l)
	for c in l:
		if c == "\n":
			#print("trailing_whitespace ok")
			continue
		if c == " ":
			rv = True
		else:
			break
	return rv


d = open(sys.argv[1]).readlines()
for line in d:
	#print ("KALA: [{}]".format(line))
	l = line.rstrip()
	#print("KALA2: [{}]".format(l))
	print (l)
		
#for line in d:
#	if trailing_whitespace(line):
#		largerv.append("\n")
#	else:
#		largerv.append(line)
#	print("".join(largerv))


