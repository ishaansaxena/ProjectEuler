#!/usr/bin/python

import math
from time import time
from collections import namedtuple
start = time()

fraction = namedtuple('fraction', 'N D')

def get_value(f):
    return float(f.N)/float(f.D)

CAP = fraction(3.0, 7.0)
LIMIT = 1000000

max_fraction = fraction(0, 1)

for i in range(1, LIMIT + 1):
    if i%CAP.D != 0:
        new_fraction = fraction(int(math.floor(get_value(CAP)*i)), i)
        if get_value(new_fraction) > get_value(max_fraction):
            max_fraction = new_fraction

print max_fraction
print time() - start, "seconds"