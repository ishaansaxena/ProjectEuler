#!/usr/bin/python

import itertools, json
from time import time
start = time()

with open('_resources/059_cipher.txt', 'r') as f:
	cipher_text = json.loads(f.read())

def decode(cipher_text, key_length, key_set, check):
    for key in itertools.product(key_set, repeat=key_length):
        message = [x^y for x, y in zip(cipher_text, itertools.cycle(key))]
        if check in ''.join(map(chr, message)):
            return sum(message)
    return "No solution"

print decode(cipher_text, 3, range(97, 123),' the ')
print time() - start, "seconds"