#!/usr/bin/python

from time import time
start = time()

"""
def gcd(a, b):
    if b == 0: 
        return a
    else:
        return gcd(b, a % b)
"""

def digit_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + digit_sum(n/10)

def get_an(n):
    if n % 3 == 0:
        return n/3*2
    else:
        return 1

def get_next_convergent(c):
    k = len(c)
    an = get_an(k + 1)
    nn = an * c[k-1][0] + c[k-2][0]
    dd = an * c[k-1][1] + c[k-2][1]
    c.append([nn, dd])

convergents = [[2, 1], [3, 1], [8, 3]]

while len(convergents) < 100:
    get_next_convergent(convergents)

print digit_sum(convergents[99][0])
print time() - start, "seconds"
