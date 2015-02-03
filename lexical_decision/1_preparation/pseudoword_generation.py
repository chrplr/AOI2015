#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time-stamp: <2015-02-03 10:54 christophe@pallier.org>

"""
Generation of pseudowords
"""

# Reads the word column from lexique_small.csv

INPUTFILE = 'lexique_small.csv'


import csv

reader = csv.reader(open(INPUTFILE, 'rb'), delimiter=',')
words = [row[1].decode('utf-8') for row in reader]

def pseudo(w):
    """ returns a  pseudo word generated from a word """
    pw = w
    return pw

for w in words:
    print w, pseudo(w)
