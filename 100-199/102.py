#!/usr/bin/python

from time import time

start = time()

def area(ax, ay, bx, by, cx, cy):
    return abs(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))

def contains_origin(t):
    ax, ay, bx, by, cx, cy = t[0], t[1], t[2], t[3], t[4], t[5]
    AT = area(ax, ay, bx, by, cx, cy)
    at1 = area(ax, ay, bx, by, 0, 0)
    at2 = area(ax, ay, 0, 0, cx, cy)
    at3 = area(0, 0, bx, by, cx, cy)
    if AT - at1 - at2 - at3 == 0:
        return True
    else:
        return False

with open("_resources/102_triangles.txt", "r") as f:
    triangles = f.readlines()

count = 0
for triangle in triangles:
    if contains_origin(map(int, triangle.strip().split(','))):
        count += 1

print count
print time() - start, "seconds"
