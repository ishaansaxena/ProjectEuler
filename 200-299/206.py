#!/usr/bin/python

from time import time
start = time()

def compare(N):
    S = str(N)
    return all(int(S[2*i]) == i+1 for i in range(9))

n = 138902663
while not compare(n*n): n -= 2

print n*10, n*n*100

print time() - start, "seconds"