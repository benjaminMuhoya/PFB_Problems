#!/usr/bin/env python3
import sys
import re

###
with open (sys.argv[1], 'r') as fasta7:
	for line in fasta7:
		gene_key = re.search(r"^>\S+\s",line)
		print('I SEARCH FOR THE UNIQUE KEY =',gene_key, line, sep = '\n')

with open (sys.argv[1], 'r') as fasta7:
	for keys in fasta7:
			key_with_subpattern = re.search(r"(^>\S+\s).?\S|", keys)
			print('I SEARCH FOR UNIQUE KEY AND INCLUDED SUB-PATTERN',key_with_subpattern, sep='\n')

##print out found stuff
with open (sys.argv[1], 'r') as fasta7:
	for unique_identifier in fasta7:
		key_unique = re.search(r"(^>\S+)\s(\s?.*$)", unique_identifier)
		if key_unique:
			print(f"id:{key_unique.group(1)}, seq:{key_unique.group(2)}", "ABOVE IS GENE_KEY AND SEQUENCE --> THIS NEEDS MORE CLEANING",sep ='\n')

###Parsing through second file
with open (sys.argv[2], 'r') as restriction:
	for sequence in restriction:
		##site = re.search(r"[CG]AATT[AT]", sequence)
		##if site:
			##print('THIS IS RESTRICTION SITES FOUND:',site)
		highlight_cut_site = re.sub(r"[CG]AATT[AT]", "^[C or G]AATT[T or A]^", sequence)
		print('FOUND SITE REPLACED WITH SYMBOL',highlight_cut_site)

####determine the length of the fragments and sort them by order
cut_sites = "" 
with open (sys.argv[2], 'r') as restriction:
	for sequence in restriction:
		highlight_cut_site = re.sub(r"[CG]AATT[AT]", "^[C or G]AATT[T or A]^", sequence)
		for identified_sites in highlight_cut_site:
			sites_in_list_format = cut_sites.join(identified_sites)
			sites_list = re.findall(r"(\.*{(^[CG]AATT[TA]^)})", sites_in_list_format)
			##print(sites_list)
			identified_split = sites_list.split(f"^[C or G]AATT[T or A]")
			print(identified_split)


