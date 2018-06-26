#!/usr/bin/python

from time import *
start = time()

"""
Reduction logic:

d6 = 0 or 5 (multiple of 5)

d6 + d8 - d7 is a multiple of 11 (d6d7d8 is a multiple of 11)

if d6 = 0
d8 = d7 (not possible)
or d8 = d7 + 11 (not possible)

Thus d6 = 5
Thus (d7, d8) belongs to {(6, 1), (7,2), (8,3), (9,4), (1,7), (2,8), (3,9)}

(10*d5 + d6 - 2*d7) is a multiple of 7 (d5d6d7 is a multiple of 7)

Putting values of d7 and d8 to get all d5s:
d5d6d7d8 belongs to {(7,5,6,1),(3,5,7,2),(6,5,8,3),(2,5,9,4),(6,5,1,7),(9,5,2,8)}

(9*d7 + 10*d8 + d9) is a multiple of 13 (d7d8d9 is a multiple of 13)

Putting d7 and d8:
d5d6d7d8d9 belongs to {(3,5,7,2,8),(9,5,2,8,6)}

(10*d8 + d9 - 5*d10) is a multiple of 17 (d8d9d10 is a multiple of 17)

Putting d8 and d9:
d5..d10 belongs to {(3,5,7,2,8,9), (9,5,2,8,6,7)}

d4 can take 0,4,6 in C1 and 0,4 in C2

d3,d4 can be 6,0 or 0,6 in C1 and 3,0 in C2 (multiple of 3)

Thus only C1 exists.

"""

t1 = [0,0,0,6,3,5,7,2,8,9]
t2 = [0,0,6,0,3,5,7,2,8,9]
t3 = [0,0,3,0,9,5,2,8,6,7]
d = [1,4]
t1.reverse()
t2.reverse()
t3.reverse()
n1 = 0
n2 = 0
n3 = 0
for i in range(10):
	n1 += t1[i]*10**i
	n2 += t2[i]*10**i
	n3 += t3[i]*10**i

s = 0

for i in d:
	for j in d:
		if i!=j:
			s += n1+n2+n3+3*i*10**9+3*j*10**8

print s

print time() - start, "seconds"