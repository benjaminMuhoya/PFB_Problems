#!/usr/bin/env python3
import sys

###Opening the file
gene_sets = {}
with open (sys.argv[1], 'r') as FASTA_file:
	for line in FASTA_file:
		gene_id,sequence = line.split('\n')
		gene_sets[gene_id] = sequence
print(gene_sets)
	
