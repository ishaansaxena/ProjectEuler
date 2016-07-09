#!/usr/bin/python

from time import *
start = time()

def mnRectandles(m, n):
    return m*(m+1)*(n)*(n+1)/4

min_error = 10000
min_ij = (0, 0)

i = 1
while True:
    j = i
    while True:
        number = mnRectandles(i, j)
        error = abs(number - 2000000)
        if error < min_error:
            min_ij = (i, j)
            min_error = error
        if j > 100:
            break
        j += 1
    if i > 100:
        break
    i += 1

print "Size: %s || Error: %d" % (min_ij, min_error)
print "Area:", min_ij[0] * min_ij[1]

print time() - start, "seconds"