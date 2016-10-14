#!/usr/bin/python

from time import *
start = time()

currency = [1, 2, 5, 10, 20, 50, 100, 200]

goal = 200
solutions = [1] + [0]*goal

for coin in currency:
	for i in range(coin, goal+1):
		solutions[i] += solutions[i-coin]

print solutions[goal]

print time() - start, "seconds"