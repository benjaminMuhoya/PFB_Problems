#!/usr/bin/env python3
import sys

my_dict = {'BOOKS' : 'EVOLUTION' , 'SONG' : 'NGOZI' , 'FRUIT' : 'MANGO'}
print(my_dict['BOOKS'])

fav_thing = 'BOOKS'
print('previous fav thing',my_dict[fav_thing], sep='\n')

print('Random print=',my_dict['FRUIT'])

###Adding new values to the dictionary
my_dict.update({'ORGANISM':'HYENA'})
fav_thing = 'ORGANISM'
print('my second fav thing=',my_dict[fav_thing], sep='\n')

###Loop to print out everything in the dictionary i.e. keys and values
for keys in my_dict:
	print(keys, ':' ,my_dict[keys])

###
###Question 7,8,9,10
