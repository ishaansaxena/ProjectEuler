#!/usr/bin/python

from time import time
start = time()

LIMIT = 1000000

N = [x for x in range(LIMIT + 1)]
P = [True] * len(N)

P[0], P[1] = False, False

for i in range(len(P)):
    if P[i]:
        n = N[i]
        N[i] = N[i] * (n - 1) / n
        for j in range(2 * i, len(P), i):
            P[j] = False
            N[j] = N[j] * (n - 1) / n

max_v = 0
max_n = 0
for i in range(1, len(N)):
    v = N[i] = float(i)/N[i]
    if v > max_v:
        max_v = v
        max_n = i

print max_n

print time() - start, "seconds"
