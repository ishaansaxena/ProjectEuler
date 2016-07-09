#!/usr/bin/python

from time import *
start = time()

def create_chain(n):
	c = [n]
	while(c[len(c)-1] != 1):
		if(n%2 == 0):
			n = n//2
		else:
			n = 3*n + 1
		c.append(n)
	return c

i = 1
m_n = 0
m_l = 0

while(i < 1000000):
	z = len(create_chain(i))
	if(z > m_l):
		m_l = z
		m_n = i
	i+=2

print m_n

print time() - start

# very long