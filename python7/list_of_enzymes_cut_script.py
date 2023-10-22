#!/usr/bin/env python3
import sys
import re

###Open downloaded bionet.txt
with open (sys.argv[1], 'r') as enzymes:
	for lines in enzymes:
		##print(lines)
		enzyme_keys = re.search(r"(^\S+\s?\W?\w+\S+\W?)\s(.*$)", lines)
		print(type(enzyme_keys))
		##if enzyme_keys:
			##print(f"id:{enzyme_keys.group(1)}, seq:{enzyme_keys.group(2)}")
		for found_keys in (r"(^\S+\s?\W?\w+\S+\W?)\s(.*$)",lines):
			print(type(found_keys)
			
			key_id = found_keys.group(1)
			seq_id = found_keys.group(2)
			##another_group_maybe = found_keys.group(3)
		print(key_id,seq_id)
##Create dictionary with keys and patterns in the bionet file


##
