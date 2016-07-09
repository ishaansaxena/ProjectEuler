#!/usr/bin/python

from time import *
start = time()

decimal = ""

for i in range(1,200000):	# Upper bound provides 1,088,889 digits
	decimal += str(i)

s  = int(decimal[1-1])
s *= int(decimal[10-1])
s *= int(decimal[100-1]) 
s *= int(decimal[1000-1])
s *= int(decimal[10000-1])
s *= int(decimal[100000-1])
s *= int(decimal[1000000-1])

print s

print time() - start, "seconds"