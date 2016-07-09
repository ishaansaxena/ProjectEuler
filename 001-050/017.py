#!/usr/bin/python

from time import *
start = time()

numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
pred = ["", "", "twen", "thir", "for", "fif", "six", "seven", "eigh", "nine"]
p_value = ["", "ty", "hundred", "thousand"]

def toNumberName(x):
	name = ""
	clone = x
	while clone > 0:
		if clone == 1000:
			name = "onethousand"
			break
		if clone/100 >= 1:
			name += numbers[clone//100]
			name += p_value[2]
			name += "and"
			clone = clone%100
		elif clone/10 >= 2:
			name += pred[clone%100//10]
			name += p_value[1]
			clone = clone%10
		else:
			name += numbers[clone]
			clone = 0
	return name

i = 1
count = 0
while i <= 1000:
	name = toNumberName(i)
	print i, name
	count += len(name)
	i+=1

count -= 3*9 # for the and

print count

print time() - start, "seconds"