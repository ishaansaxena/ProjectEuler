#!/usr/bin/python

from time import *
start = time()

def isPrime(x):
	if(x == 2):
		return True
	elif(x < 2):
		return False
	else:
		i = 2
		while(i < x//2 + 1):
			if(x%i ==0):
				return False
			else:
				pass
			i+=1
		return True

def primeFactors(n):
	i = 2
	while(i < n):
		if (n%i == 0 and isPrime(i)):
			print (i)
			while(n%i == 0):
				n = n / i 	# reducing problem size
			n = int(n*i)
		if(n == 1):
			break
		i+=1

primeFactors(600851475143)

print time() - start, "seconds"