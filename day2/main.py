import csv
''' part one
password = []
passwords = []

with open ('day2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar= '|')
    for row in spamreader:
        row[0] = row[0].split('-')
        password.append(row[0][0])      # minChars
        password.append(row[0][1])      # maxChars
        password.append(row[1][:-1])    # requiredChar
        password.append(row[2])         # password
        passwords.append([password[0], password[1], password[2], password[3]])
        password.clear()

i = 0

for row in passwords:
    if int(row[0]) <= int(row[3].count(row[2])) <= int(row[1]):
        i+=1

print(i)                                # number of valid passwords
'''

# part two

password = []
passwords = []

with open ('day2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar= '|')
    for row in spamreader:
        row[0] = row[0].split('-')
        password.append(row[0][0])      # minChars
        password.append(row[0][1])      # maxChars
        password.append(row[1][:-1])    # requiredChar
        password.append(row[2])         # password
        passwords.append([password[0], password[1], password[2], password[3]])
        password.clear()

i = 0   # number of letter matches in one password
j = 0   # number of valid passwords

for row in passwords:
    if row[3][int(row[0])-1] == row[2]:     # is letter at position 1
        i += 1
    if row[3][int(row[1])-1] == row[2]:     # is letter at position 2
        i += 1
    if i == 1:  # letter should only be at one of the 2 positions
        j += 1
    i = 0

print(j)