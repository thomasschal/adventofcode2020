import csv
from typing import List

numbers = []

with open ('day1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar= '|')
    for row in spamreader:
        numbers.append(int(row[0]))
''' part 1
for i in numbers:
    for j in numbers:
        if j >= i:
            if i + j == 2020:
                print(i,j,i*j)
'''
for i in numbers:
    for j in numbers:
        if j >= i:
            for k in numbers:
                if k >= j:
                    if i + j + k == 2020:
                        print(i,j,k,i*j*k)
                        break
