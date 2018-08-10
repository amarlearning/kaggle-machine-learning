## 1. Introduction to Modules ##

from math import sqrt, floor

root = sqrt(99)
flr = floor(89.9)

## 2. Importing Using An Alias ##

import math as m

root = m.sqrt(33)

## 3. Importing A Specific Object ##

from math import sqrt

root = sqrt(1001)

## 4. Variables Within Modules ##

import math

print(math.pi)

a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)

## 5. The CSV Module ##

import csv

f = open("nfl.csv", "r")
nfl = list(csv.reader(f))

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))

def count_value_col(value, col):
    patriots_wins = 0
    for data in nfl:
        if data[col] == value:
            patriots_wins += 1
            
    return patriots_wins

patriots_wins = count_value_col("New England Patriots", 2)

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(value):
    patriots_wins = 0
    for data in nfl:
        if data[2] == value:
            patriots_wins += 1
            
    return patriots_wins

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")
