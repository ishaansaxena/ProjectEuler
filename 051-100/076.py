#!/usr/bin/python
# Code exactly same as 031, tweaked a bit.

from time import *
start = time()

target_number = 100
number_pool = [i for i in range(1, target_number)]

solutions = [1] + [0]*target_number

for i in number_pool:
	for j in range(i, target_number+1):
		solutions[j] += solutions[j-i]

print solutions[target_number]

print time() - start