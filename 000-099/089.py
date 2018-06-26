#!/usr/bin/python

from time import time

numerals = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

def integer_to_roman(n, r=""):
    if n > 0:
        if n >= 1000:
            r += "M"
            n -= 1000
            return integer_to_roman(n, r)
        elif n >= 900:
            r += "CM"
            n -= 900
            return integer_to_roman(n, r)
        elif n >= 500:
            r += "D"
            n -= 500
            return integer_to_roman(n, r)
        elif n >= 400:
            r += "CD"
            n -= 400
            return integer_to_roman(n, r)
        elif n >= 100:
            r += "C"
            n -= 100
            return integer_to_roman(n, r)
        elif n >= 90:
            r += "XC"
            n -= 90
            return integer_to_roman(n, r)
        elif n >= 50:
            r += "L"
            n -= 50
            return integer_to_roman(n, r)
        elif n >= 40:
            r += "XL"
            n -= 40
            return integer_to_roman(n, r)
        elif n >= 10:
            r += "X"
            n -= 10
            return integer_to_roman(n, r)
        elif n == 9:
            r += "IX"
            n -= 9
            return integer_to_roman(n, r)
        elif n >= 5:
            r += "V"
            n -= 5
            return integer_to_roman(n, r)
        elif n == 4:
            r += "IV"
            n -= 4
            return integer_to_roman(n, r)
        else:
            r += "I"
            n -= 1
            return integer_to_roman(n, r)
    else:
        return r

def roman_to_integer(r):
    if len(r) > 1:
        c0 = numerals[r[0]]
        c1 = numerals[r[1]]
        if c0 >= c1:
            return c0 + roman_to_integer(r[1:])
        else:
            return c1 - c0 + roman_to_integer(r[2:])
    elif len(r) == 1:
        return numerals[r[0]]
    else:
        return 0

if __name__ == '__main__':

    start = time()    

    with open('_resources/089_roman.txt') as f:
        text = f.readlines()

    s = ""
    t = ""
    for line in text:
        s += integer_to_roman(roman_to_integer(line[:-1]))
        t += line[:-1]

    print len(t) - len(s)

    print time() - start, "seconds"

