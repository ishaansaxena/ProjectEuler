#!/usr/bin/python

from time import *
start = time()

fib = [1,2]
sum = 2

while(fib[len(fib)-1]<=4000000):
	fib.append(fib[len(fib)-1]+fib[len(fib)-2])
	if(fib[len(fib)-1]%2 == 0):
		sum+=fib[len(fib)-1]

print sum

print time() - start, "seconds"