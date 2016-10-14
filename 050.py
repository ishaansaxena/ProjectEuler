#!/usr/bin/python

from time import *
start = time()

c_end = 1000000

sieve = [True] * c_end
sieve[0] = sieve[1] = False

for num in range(len(sieve)):
	if sieve[num]:
		for multiple in range(2*num, len(sieve), num):
			sieve[multiple] = False;

p_list = [i for i in range(len(sieve)) if sieve[i]]

p_sum = [0] * len(p_list)
p_sum[0] = 2

i = 1

while i < len(p_sum):
	p_sum[i] = p_sum[i-1] + p_list[i]
	if p_sum[i-1] in p_list:
		print i, p_sum[i-1]
	i+=1
	if p_sum[i] > c_end:
		break 

if p_sum[i-1] in p_list:
		print i, p_sum[i-1]

print time() - start, "seconds"