#!/usr/bin/python

from time import *
start = time()

main = []

def digitCount(x):
	if x == 0:
		return 0
	else:
		return 1 + digitCount(x//10)

def isPandigital(x):
	n = range(1,10)
	clone = x
	while len(n) != 0:
		if clone%10 in n:
			n.remove(clone%10)
		else:
			return False
		clone = clone//10
	return True

def multiPairX(x):
	y = 1
	z = 0
	xyz = 0
	while digitCount(xyz) < 9:
		z = x*y
		xyz = int(str(x)+str(y)+str(z))
		y += 10
	y-=10
	while digitCount(xyz) < 10:
		z = x*y
		xyz = int(str(x)+str(y)+str(z))
		if isPandigital(xyz):
			if z in main:
				pass
			else:
				main.append(z)
		y += 1

for i in range(1,32000):
	multiPairX(i)

result = 1
for n in main:
	result += n

print result-1

print time() - start, "seconds"