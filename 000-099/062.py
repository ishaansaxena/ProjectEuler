#!/usr/bin/python

from time import time
start = time()

LIMIT = 10000

MAP_P_TO_NUM   = {}
MAP_P_TO_COUNT = {}

n = 1
while True:
    cube = str(n ** 3)
    cstr = "".join(sorted(cube))

    if cstr not in MAP_P_TO_NUM:
        MAP_P_TO_NUM[cstr] = cube

    if cstr not in MAP_P_TO_COUNT:
        MAP_P_TO_COUNT[cstr] = 1
    else:
        MAP_P_TO_COUNT[cstr] += 1
        if MAP_P_TO_COUNT[cstr] >= 5:
            print MAP_P_TO_NUM[cstr]
            break

    n += 1
    if n > LIMIT:
        break

print time() - start, "seconds"
