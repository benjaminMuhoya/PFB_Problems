#!/usr/bin/env python3
import sys

###line count
with open (sys.argv[1], 'r') as Python_06_fastq:
##pattern found in data GGCTAC [when you look inside the 
### summing up the numbers using for loops
	num_lines = sum(1 for line in Python_06_fastq)
	print('Total lines = ',num_lines, sep='\t')

###character count
character_count = []
with open (sys.argv[1], 'r') as Python_06_fastq:
	for line in Python_06_fastq:
		char_count = len(line)
		character_count.append(char_count)
	print(sum(character_count), 'is the sum of characters')
	average = sum(character_count)/len(character_count)
	print(average, 'average length of each line')
