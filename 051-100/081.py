#!/usr/bin/python

from time import time
start = time()

with open('_resources/081_matrix.txt', 'r') as f:
    matrix = [map(int, line.strip().split(',')) for line in f.readlines()]

SIZE = len(matrix)

i = SIZE - 1
j = SIZE - 1

for i in range(SIZE - 2, -1, -1):
    matrix[i][SIZE - 1] += matrix[SIZE - 1][i+1]
    matrix[SIZE - 1][i] += matrix[i+1][SIZE - 1]

for i in range(SIZE - 2, -1, -1):
    for j in range(SIZE - 2, -1, -1):
        matrix[i][j] += min([matrix[i+1][j], matrix[i][j+1]])

print matrix[0][0]

print time() - start, "seconds"