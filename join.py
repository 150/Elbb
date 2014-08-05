#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

captial = {}
adjectival = {}

with open('iso3166.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        captial[row[3]] = row[4]

with open('n-adj.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        adjectival[row[0]] = row[1]

for country, cap in captial.iteritems():
    print "%s-%s" % (adjectival.get(country, ''), cap)