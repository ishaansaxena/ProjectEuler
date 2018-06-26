#!/usr/bin/python

from time import *
start = time()

def isPallindrome(n):
	rev = []
	num = n
	while(num != 0):
		rev.append(num%10)
		num = num//10
	count = 0
	r_num = 0
	while(len(rev) > 0):
		r_num += rev[len(rev)-1]*(10**count)
		count += 1
		rev.pop()
	if(n == r_num):
		return True
	else:
		return False

num_a = 999
p = []

while(num_a >= 900):
	num_b = 999
	while (num_b >= 900):	
		if (isPallindrome(num_a*num_b)):
			p.append(num_a*num_b)
			break
		num_b-=1
	num_a-=1

p.sort(None,None,True)
print p[0]

print time() - start, "seconds"