#!/usr/bin/python

from time import *
start = time()

def leapCondition(y):
	if y%100 == 0:
		if y%400 == 0:
			return True
		else:
			return False
	else:
		if y%4 == 0:
			return True
		else:
			return False

yearmap = {}
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
y_leap = [3, 2, 1, 1, 2, 1, 1]
n_leap = [2, 2, 2, 1, 3, 1, 1]

year = 1901
firstDay = 1
count = 0
while year <= 2001:
	constraint = leapCondition(year)
	if constraint:
		firstDay = (firstDay + 2)%7
		count += y_leap[firstDay]
	else:
		firstDay = (firstDay + 1)%7
		count += n_leap[firstDay]
	year += 1

print count

print time() - start, "seconds"