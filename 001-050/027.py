#!/usr/bin/python

from time import *
from math import *
start = time()

sieve = [True] * 1000
sieve[0] = False
sieve[1] = False

def mark(e_sieve, num):
	for x in xrange(num+num, len(e_sieve), num):
		e_sieve[x] = False

def isPrime(x):
	for i in range(2,int(sqrt(x))+1):
		if x%i == 0:
			return False
	return True

def f(x,m,n):
	return x**2 + m*x + n

for i in range(len(sieve)):
	if sieve[i]:
		mark(sieve, i)

arr_a = []
arr_b = [i for i in range(len(sieve)) if sieve[i]]
res = {}

for i in range(len(arr_b)):
	arr_a.append(-arr_b[i])
	arr_a.append(arr_b[i])

arr_a.sort()

for a in arr_a:
	for b in arr_b:
		res[a,b] = []
		i = 0
		while True:
			quad = f(i,a,b)
			if quad > 0 and isPrime(quad):
				res[a,b].append(quad)
				i+=1
			else:
				break

max_len = 0
max_str = []
for line in res:
	if(len(res[line])) > max_len:
		max_len = len(res[line])
		max_str = line

print max_str[0]*max_str[1]

print time() - start, "seconds"