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
    return word[:p] + random.choice(ALLLETTERS) + word[(p + 1):]


if __name__ == '__main__':
    for i in range(20):
        print generate_pseudo2('bonjour')
