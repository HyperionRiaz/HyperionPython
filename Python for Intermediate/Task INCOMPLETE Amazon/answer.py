#!/usr/bin/python

import sys

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

for i in range (len(sys.argv)):
	if i == 0:
		continue
	else:
		ofile = open(sys.argv[i], 'r+')

	
