#!/usr/bin/python
from time import *
start = time()

def returnDigitized(x):
	arr = []
	clone = x
	while clone!=0:
		arr.append(clone%10)
		clone = clone//10
	return arr

def checkNY(Y,N):
	a_1 = returnDigitized(Y)
	a_2 = returnDigitized(N*Y)
	a_1.sort()
	a_2.sort()
	return a_1 == a_2

i = 1
while True:
	if checkNY(i,2):
		if checkNY(i,3):
			if checkNY(i,4):
				if checkNY(i,5):
					if checkNY(i,6):
						print i
						break
	i+=1

print time() - start, "seconds"