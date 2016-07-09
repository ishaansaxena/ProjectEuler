#!/usr/bin/python

from time import *
start = time()

fib = [1,1]
digits = 1000

i = 2
while(fib[i-1]/10**(digits-1) < 1):
	fib.append(sum(x for x in fib[0:len(fib)-1])+1)	#t_n = sum(1 to n-2) + 1
	i+=1

print len(fib)

print time() - start, "seconds"