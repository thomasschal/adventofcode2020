import math
import csv

mass = []
result = 0
grandResult = 0

with open ('day1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar= '|')
    for row in reader:
        mass.append(int(row[0]))

for module in mass:
    result += math.floor(module / 3) - 2
# part one = print(result); remove part below completely
    while result+result != result:
        print(result)
        grandResult += result
        result = math.floor(result / 3) - 2
        if result < 0:
            result = 0

print(grandResult)  # part two