#!/usr/bin/env python3
import sys

##
ecol_dict = {}
sequence = []
with open (sys.argv[1], 'r') as ecoli:
	for line in ecoli:
		line = line.rstrip()
		##print(line)
		if line.startswith('>'):
			key = line
			ecol_dict[key] = []
		else:
			ecol_dict[key] = line
	print(ecol_dict)
