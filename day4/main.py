'''
requiredKeys = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:'] # cid not needed
fieldsFound = 0
counter = 0

passports = []

with open('day4.txt', 'r') as passportFile:
    for line in passportFile:
        passports.append(line[:-1])

for passport in passports:
    if len(passport) == 0:
        if fieldsFound >= 7:
            counter += 1
        fieldsFound = 0
    else:
        for key in requiredKeys:
            if key in passport:
                fieldsFound += 1

print(counter)
'''

import re
from time import *

requiredKeys = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:'] # cid not needed
fieldsFound = 0
counter = 0
validEcl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def checkByr(key):
    if 1920 <= int(key) <= 2002:
        return True
    else:
        return False

def checkIyr(key):
    if 2010 <= int(key) <= 2020:
        return True
    else:
        return False

def checkEyr(key):
    if 2020 <= int(key) <= 2030:
        return True
    else:
        return False

def checkHgt(key):
    if key.endswith('cm') or key.endswith('in'):
        if key.endswith('cm') and (150 <= int(key[:-2]) <= 193):
            return True
        elif key.endswith('in') and (59 <= int(key[:-2]) <= 76):
            return True
        else:
            return False

def checkHcl(key):
    if key.startswith('#') and len(key) == 7:
        pattern = re.compile("[A-Fa-f0-9]+")
        if pattern.fullmatch(key[1:]) is None:
            return False
        else:
            return True

def checkEcl(key):
    if any(ecl in key for ecl in validEcl):
        return True
    else:
        return False

def checkPid(key):
    if key.isnumeric() and len(key) == 9:
        return True
    else:
        return False

passports = []

with open('day4.txt', 'r') as passportFile:
    for line in passportFile:
        passports.append(line[:-1])

for passport in passports:
    if len(passport) == 0:
        if fieldsFound >= 7:
            counter += 1
        fieldsFound = 0
    else:
        for key in requiredKeys:
            if key in passport:
                valueStart = passport.find(key)+len(key)
                if passport.find(' ', valueStart) == -1:
                    valueEnd = passport.find('\n', valueStart)
                    value = passport[valueStart:]
                else:
                    valueEnd = passport.find(' ', valueStart)
                    value = passport[valueStart:valueEnd]
                if key == requiredKeys[0]:
                    if checkByr(value):
                        fieldsFound += 1
                elif key == requiredKeys[1]:
                    if checkIyr(value):
                        fieldsFound += 1
                elif key == requiredKeys[2]:
                    if checkEyr(value):
                        fieldsFound += 1
                elif key == requiredKeys[3]:
                    if checkHgt(value):
                        fieldsFound += 1
                elif key == requiredKeys[4]:
                    if checkHcl(value):
                        fieldsFound += 1
                elif key == requiredKeys[5]:
                    if checkEcl(value):
                        fieldsFound += 1
                elif key == requiredKeys[6]:
                    if checkPid(value):
                        fieldsFound += 1

print(counter)