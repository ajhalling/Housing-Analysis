import os
import sys
import csv

path = '/Python/Housing-Analysis/Housing-Analysis/Tokyo.csv'

with open(path, 'r', errors='ignore') as infile, open(path + 'final.csv', 'w') as outfile:
    inputs = csv.reader(infile)
    output = csv.writer(outfile)

    i = next(inputs)
    print(str(i))
    j = next(inputs)
    print(j)