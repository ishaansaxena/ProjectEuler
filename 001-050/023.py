#!/usr/bin/python

from time import *
from math import *
start = time()

numbers = {
	0 : [],		# Abundant
	1 : []		# Non-abundant
}

def ret_divisors(n):
	x = 0
	for i in range(1,int(sqrt(n)+1)):
		if n%i == 0:
			x += i
			if i != n/i:
				x += n/i
	return x-n

sieve = [True] * 28123

for i in range(1,28124):
	if ret_divisors(i) > i:
		numbers[0].append(i)
	else:
		numbers[1].append(i)
	j = 0
	r = len(numbers[0])
	while j < r:
		if numbers[0][j] + numbers[0][r-1] == i:
			sieve[i-1] = False
			break
		elif numbers[0][j] + numbers[0][r-1] < i:
			j += 1
		else:
			r -= 1

na_sum = 0

for i in range(len(sieve)):
	if(sieve[i]):
		na_sum += i+1

print na_sum

print time() - start, "seconds"