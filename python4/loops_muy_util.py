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
