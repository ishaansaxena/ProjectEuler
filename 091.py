#!/usr/bin/python
from time import *
from math import *
from collections import namedtuple
start = time()

c_end = 50

C = namedtuple("C", "x y")
pointList = []

for i in range(c_end+1):
	for j in range(c_end+1):
		if (i,j) != (0,0):
			pointList.append(C(i, j))

def returnModList(P,Q):
	modList = [P.x**2 + P.y**2, Q.x**2 + Q.y**2, (P.x - Q.x)**2 + (P.y - Q.y)**2]
	return modList

def evalModList(P,Q):
	L = returnModList(P,Q)
	L.sort()
	if L[0] + L[1] == L[2]:
		return True
	return False

# pointCount = len(pointList)
# selectionCount = factorial(pointCount)/(factorial(3)*factorial(pointCount-3))

solutionList = []

for P in pointList:
	for Q in pointList:
		if evalModList(P,Q) and P.y - P.x < Q.y - Q.x:
			solutionList.append((P,Q))

print len(solutionList)//2

print time() - start, "seconds"