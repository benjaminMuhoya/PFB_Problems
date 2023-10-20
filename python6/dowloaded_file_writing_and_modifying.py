#!/usr/bin/env python3
import sys

##Reading with first method
with open (sys.argv[1], "r") as Downloaded_git_file:
	print(Downloaded_git_file)
	for line in Downloaded_git_file:
		line = line.rstrip()
		print(line)

###Open the file in the second method

with open (sys.argv[1], "r") as Downloaded_git_file:
	contents_of_file = Downloaded_git_file.read()
	print(contents_of_file, "in upper case", contents_of_file.upper(), sep='\n')


###
