#!/usr/bin/env python3
import sys
import re

###
sequence_dict = {}
whole_file =[]
with open (sys.argv[1], 'r') as python8:
	for line in python8:
		whole_file.append(line)
		if whole_file.startswith('>'):
			key_gene_id = whole_file.split
			print(key_gene_id)
	##print(whole_file)
		##print(line, type(line))
		##gene_id,sequence = line.split('\n')
		##sequence_dict[gene_id]=sequence
##print(sequence_dict, sep='\n')

		##for sequences in (r"(^>\S+\s?).+([ACTG]+\S\s?).?$", line):
