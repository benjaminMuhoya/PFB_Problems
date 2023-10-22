#!/usr/bin/env python3
import sys
import re
import argparse

with open (sys.argv[1], 'r') as python_07_first:
	for line in python_07_first:
		pattern_to_search_info = re.search(r"Nobody", line)
		##print(pattern_to_search_info)
		substituted_nobody_with_Benja = re.sub(r"Nobody", "Benjamin", line)
		print(substituted_nobody_with_Benja)
