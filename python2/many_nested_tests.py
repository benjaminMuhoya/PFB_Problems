#!/usr/bin/env python3
import sys

test = 55
if test <50:
	message = 'smaller than 50'
	print(test, message)
elif test %3==0:
	message = 'divisible by 3'
	print(test, message)
else:
	message = 'Greater than 50 and not divisible by 3'
	print(test, message)
