# -*- coding: utf-8 -*-
#!/usr/bin/python
from time import *
start = time()

LIMIT = 1000

# Pell's Equation
# x(k) = x(0)x(k-1) + Dy(0)y(k-1)
# y(k) = x(0)y(k) + y(0)x(k)
# To find x0 and y0:
# See H.W. Lenstra Jr.'s paper on solving Pell Equations

def isSquare(x):
	return x**0.5 == x**0.5 - x**0.5%1.0

result = 0
x_max = 0

for D in range(2,LIMIT+1):
	if isSquare(D):
		continue
	L_val = int(D**0.5)
	M_val = 0
	d = 1
	a = L_val
	x_0 = 1
	x = a
	y_0 = 0
	y = 1
	while x*x - y*y*D != 1:
		M_val = d * a - M_val
		d = (D - M_val * M_val) / d
		a = (L_val + M_val) / d
		x_1 = x_0
		x_0 = x
		y_1 = y_0
		y_0 = y
		x = a*x_0 + x_1
		y = a*y_0 + y_1
	if x > x_max:
		x_max = x
		result = D

print result

print time() - start, "seconds"