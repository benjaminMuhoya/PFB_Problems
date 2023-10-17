#!/usr/bin/env python3
import sys

test =float(sys.argv[1])
print(type(test))
if test <0:
	message='negative'
	print(test, message)
elif test == 0:
	message='it is zero'
	print(test, message)
elif test <50:
	message='smaller than 50'
	print(test, message)
elif test %3==0:
	message='not even'
	print(test, message)
elif test >50:
	message='larger than 50'
	print(test, message)
else:
	message='it is 50 and divisible by 2'
	print(test, message)
