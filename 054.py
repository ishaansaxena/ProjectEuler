#!/usr/bin/python

from collections import Counter
from time import time
start = time()

with open('_resources/054_poker.txt', 'r') as f:
    raw_data = f.readlines()
    hands = [line.strip().split(" ") for line in raw_data]

card_values = {j: i for i, j in enumerate('23456789TJQKA', start=2)}
straight_pairs = [(i, i-1, i-2, i-3, i-4, i-5) for i in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

def rank_hand(hand):
    score = zip(*sorted(((j, card_values[i]) for i,j in Counter(c[0] for c in hand).items()), reverse=True))
    score[0] = ranks.index(score[0])
    if len(set(card[1] for card in hand)) == 1: 
        score[0] = 5
    if score[1] in straight_pairs: 
        score[0] = 8 if score[0] == 5 else 4
    return score

print sum(rank_hand(hand[:5]) > rank_hand(hand[5:]) for hand in hands)

print time() - start, "seconds"