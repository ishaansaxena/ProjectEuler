#!/usr/bin/python

import decimal
from time import time
start = time()

decimal.getcontext().prec = 102

def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number%10 + sum_of_digits(number/10)

s = 0
for i in range(1,100):
    root = str(decimal.Decimal(i)**decimal.Decimal(0.5))
    root = int(root[root.index('.')+1:])
    s += sum_of_digits(root)

print s
print time() - start, "seconds"