#!/usr/bin/python

from time import time
start = time()

TARGET = 1000000
P = []
P.append(1)

n = 1
while True:
    i = 0
    penta = 1
    P.append(0)
    while penta <= n:
        sign = -1 if (i % 4 > 1) else 1
        P[n] += sign * P[n - penta]
        P[n] %= TARGET;
        i += 1
        j = (i / 2 + 1) if (i % 2 == 0) else -(i / 2 + 1)
        penta = j * (3 * j - 1) / 2
    if P[n] == 0:
        break
    n += 1

print n
print time() - start, "seconds"