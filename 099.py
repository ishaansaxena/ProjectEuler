#!/usr/bin/python

import math
from time import time
start = time()

max_exponent = (0, 0)

with open('_resources/099_base_exp.txt', 'r') as f:
    counter = 0
    readable = True
    while readable:
        try:
            counter += 1
            base_exp_pair = map(int, f.readline().split(','))
            new_exponent = base_exp_pair[1] * math.log(base_exp_pair[0])
            if new_exponent > max_exponent[1]:
                max_exponent = (counter, new_exponent)
        except:
            readable = False

print max_exponent
print time() - start, "seconds"