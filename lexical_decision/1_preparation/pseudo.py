#! /usr/bin/env python
# -*- coding: utf-8 -*-


import random

ALLLETTERS = u"abcdefghijklomnopqrstuvwxyzéèôê"


def generate_pseudo(size):
    s = u''
    for i in range(size):
        s = s + random.choice(ALLLETTERS)
    return s


def generate_pseudo2(word):
    n = len(word)
    p = random.randint(0, n - 1)
    while True:
        pw = word[0:p] + random.choice(ALLLETTERS) + word[(p + 1):n]
        if pw != word:
            break
    return(pw)

if __name__ == '__main__':
    import sys
    for line in sys.stdin:
        word = line.rstrip().decode('utf-8')
        print generate_pseudo2(word).encode('utf-8')
