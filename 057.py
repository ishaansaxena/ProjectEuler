#!/usr/bin/python

from time import time
start = time()

LIMIT = 1000

pd = 2
pn = 3

count = 0
for i in range(LIMIT):
    pd, pn = pd + pn, 2*pd + pn
    if len(str(pn)) > len(str(pd)):
        count += 1

print count
print time() - start, "seconds"