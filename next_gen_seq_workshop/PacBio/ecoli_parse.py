#!/usr/bin/env python3
import sys
import re
from Bio.Seq import Seq
from Bio import SeqIO

###Create an empty dictionary first
empty_dict = {}
##Use the bioseq module to parse the file
for sequence_records in SeqIO.parse(sys.argv[1], "fasta"):
	if sequence_records:
		contig_len = len(sequence_records)
		ID_s = sequence_records.id
		empty_dict[ID_s] = contig_len
dict(sorted(empty_dict.items(), key=lambda item: item[1]))
print(empty_dict)
	##print('SEQUENCE', sequence_records.seq)
		
