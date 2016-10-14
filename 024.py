#!/usr/bin/python

from time import *
from math import *
start = time()

digits = [0,1,2,3,4,5,6,7,8,9]
index = 1000000

def permute(array, i):
	if(len(array) > 0):
		f = factorial(len(array)-1)
		n = int(ceil(i//f))
		print array[n],
		array.remove(array[n])
		permute(array,i-n*f)

permute(digits, index-1)

print ""
print time() - start, "seconds"