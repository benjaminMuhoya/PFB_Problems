#!/usr/bin/env python3
import sys

gene_keys_empty = {}

###
with open (sys.argv[1], 'r') as another_download: ## the file is in 'name\tsequence\n' format
	for sequence in another_download:
		sequence = sequence.rstrip()
		gene_id,seq = sequence.split('\t')
		gene_keys_empty[gene_id]=seq
print(gene_keys_empty, sep='\n')



####
with open (sys.argv[1], 'r') as another_download: ## the file is in 'name\tsequence\n' format
	for sequence in another_download:
		sequence = sequence.rstrip()
		gene_id,seq = sequence.split('\t')

for seq in gene_keys_empty:
	dna_complement = gene_keys_empty[seq].upper().replace('T','a').replace('A','t').replace('C','g').replace('G','c')
	reverse_complement_of_each_gene = dna_complement[::-1].upper()
	print(reverse_complement_of_each_gene)

for seq in gene_keys_empty:
	print('>'+seq) ##Printing in FASTA file format
	print(gene_keys_empty[seq])
##
