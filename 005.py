#!/usr/bin/python

from time import *
from math import *
start = time()

def isPrime(x):
	i = 2
	while(i < int(sqrt(x)) + 1):
		if(x%i ==0):
			return False
		else:
			pass
		i+=1
	return True

n = 20
numbers = {}
primes = [2,3,5,7,11,13,17,19]
product = 1

for i in range(1,n+1):
	numbers[i] = {}

for i in numbers:
	num = i
	for j in primes:
		numbers[i][j] = 0
		while(num >= j and num %j == 0 and num != 1):
			numbers[i][j] += 1
			num = num // j

arr = []

for j in primes:
	i = 1
	flag = numbers[1][j]
	while(i < n+1):
		if(flag < numbers[i][j]):
			flag = numbers[i][j]
		i += 1
	arr.append(flag)

i = 0
while (i < 8):
	product *= primes[i]**arr[i]
	i+=1

print product

print time() - start, "seconds"