import os
import csv

data = csv.reader(open('Tokyo.csv'))

for row in data:
    print(row)