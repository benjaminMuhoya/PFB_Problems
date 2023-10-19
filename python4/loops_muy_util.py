#!/usr/bin/env python3
import sys
##Part 1
human_taxa = 'sapiens, erectus, neanderthalensis'
print('STRING PRINT OUT',human_taxa,'WHAT IS IN [1]',human_taxa[1],'CLASS OF THE OBJECT',type(human_taxa), sep='\n')

##Part 2

split_taxa = human_taxa.split(', ')
print('OUTPUT OF SPLIT',split_taxa,'WHAT IS IN [1]' ,split_taxa[1],'CLASS OF THE OBJECT', type(split_taxa), sep='\n')

##Part 3 sort alphabetically
taxa_sorted = sorted(split_taxa, key=str.lower)
taxa_len_sort = sorted(split_taxa, key=len)
print('SORTED ALPHABETICALLY',taxa_sorted,'SORTED BY LENGTH', taxa_len_sort, sep='\n')

###Loop to print out the numbers 1 to 100
count = 0
while count < 101:
	print(count)
	count+=1

###Loop to calculate the factorial of 1000
count = 1
previous_count = 1
while count <1001:
	factorial_result = count*previous_count
	previous_count = factorial_result
	count+=1
	if count == 1000:
		break
	print('current factorial is =', factorial_result)
print('done')

###Iterate through each number in a sequence
my_sequence = [101,2,15,22,95,33,2,27,72,15,52]
for number in my_sequence:
	if number %2 == 0:
		print('this is an even number', number)
