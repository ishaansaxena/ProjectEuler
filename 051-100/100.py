#!/usr/bin/python
from time import *
from math import sqrt
start = time()

p = 12
c_upper = 10**p

blue = 15
total = 21

while total < c_upper:
	new_blue = 3*blue + 2*total - 2
	new_total = 4*blue + 3*total - 3
	blue = new_blue
	total = new_total

print blue

print time() - start, "seconds"