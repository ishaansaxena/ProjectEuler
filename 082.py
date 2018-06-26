#!/usr/bin/python

import numpy as np
from time import time

SIZE = 5

start = time()

file = open('_resources/082_matrix.txt', 'r')
m = []

for line in file:
	l = map(int, line.strip().split(","))
	m.append(l)

matrix = np.array(m)

print matrix

sums = [matrix[i, SIZE - 1] for i in range(SIZE)]
 
for i in range(SIZE - 2, -1, -1):
	sums[0] += matrix[0, i]
	for j in range(1, SIZE):
		sums[j] = min([sums[j-1] + matrix[j, i], sums[j] + matrix[j, i]])
	for j in range(SIZE - 2, -1, -1):
		sums[j] = min([sums[j], sums[j+1] + matrix[j, i]])

print min(sums)

print time() - start, "seconds"
