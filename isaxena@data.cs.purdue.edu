#!/usr/bin/python

from time import *
start = time()

SIZE = 4000000

z = [0] * SIZE

def create_chain(n):
	c = 0
	while (n != 1):
		if n < SIZE and z[n] != 0:
			return c + z[n]
		if n % 2 == 0:
			n = n//2
		else:
			n = 3 * n + 1
		c += 1
	return c

i = 1
m_n = 0
m_l = 0

while(i < SIZE):
	s = create_chain(i)
	z[i] = s
	if(s > m_l):
		m_l = s
		m_n = i
	i+=2

print m_n

print time() - start, "seconds"

# somewhat long