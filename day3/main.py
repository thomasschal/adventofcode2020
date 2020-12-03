from array import *
import csv
from time import *

map = []

def collisions(steps,jumps):
    counter = 0
    index = 2
    x = 0
    for line in map:
        if index % jumps == 0:
            if line[x % len(line)] == '#':
                counter += 1
            x += steps
        index += 1
    return counter


with open ('day3.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar= '|')
    for row in spamreader:
        map.append(str(row[0]))

print(collisions(1,1))
print(collisions(3,1))
print(collisions(5,1))
print(collisions(7,1))
print(collisions(1,2))

print(collisions(1,1) * collisions(3,1) * collisions(5,1) * collisions(7,1) * collisions(1,2))




