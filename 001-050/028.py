#!/usr/bin/python

from time import *
start = time()

center = 1
offset = 2
rows = 1001

diagonal_numbers = [1]

carry = center
while(offset < rows):
	j = 0
	while(j < 4):
		carry += offset
		diagonal_numbers.append(carry)
		j+=1
	offset+=2

print sum(diagonal_numbers)

print time() - start, "seconds"