#!/usr/bin/env python3
import sys
import re
from Bio.Seq import Seq
from Bio import SeqIO

##Create empty Dict
empty_dict = {}
##Open file using bioseq
for sequences in SeqIO.parse(sys.argv[1], "fasta"):
	if sequences:
		contig_ids = sequences.id
		sequences = sequences.seq
		##Turn the sequences into a set for easy counting
		seq_set = set(sequences)
	print(contig_ids)
	for gtca in seq_set:
		count_no =sequences.count(gtca)
		##append the count_no to a dictionary
		empty_dict[gtca]=count_no
	print('nucleotide count=', empty_dict)

###Getting the contig count
with open (sys.argv[1], 'r') as fruity:
	for lines in fruity:
		if lines.startswith('>'):
			total = lines
			##contig_count = len(lines.readlines())
	print("this is the total number of contigs",len(total))
