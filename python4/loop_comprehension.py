#!/usr/bin/env python3
import sys

my_seq_nums = [101,2,15,22,95,33,2,27,72,15,52]
for nums in my_seq_nums:
	if nums %2 == 0:
		print('Number is even',nums)
###
my_seq_sorted = sorted(my_seq_nums)
for nums in my_seq_sorted:
	print(nums)

###
even_nums = []
odd_nums = []
for nums in my_seq_nums:
	if nums %2 == 0:
		even_nums.append(nums)
	else:
		odd_nums.append(nums)
print('Done seperating even and odd')

sum_of_odds = sum(odd_nums)
sum_of_evens = sum(even_nums)
print('Summing up odds',sum_of_odds, 'sum of evens =',sum_of_evens, sep='\n') 
