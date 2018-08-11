## 1. Introduction ##

# Stream column for top 5 songs only
top5_streams = [2993988783, 1829621841, 1460802540, 1386258295, 1311243745]

def average(top5_streams):
    return sum(top5_streams)/len(top5_streams)

total_average = average(top5_streams)

## 2. Introduction to Modules ##

import statistics

top5_streams = [2993988783, 1829621841, 1460802540, 1386258295, 1311243745]

average = statistics.mean(top5_streams)

## 3. Loading our data using the CSV module ##

import csv

f = open("top100.csv", "r")
csvreader = csv.reader(f)

music = list(csvreader)

## 4. Understanding the namespace ##

import math, statistics

dir(statistics)

## 5. Cleaning Our Data ##

import csv

track_names = []
stream_numbers = []
f = open("top100.csv","r")
music = list(csv.reader(f))

for data in music[1:len(music)]:
    track_names.append(data[0])
    stream_numbers.append(int(data[3]))

## 6. Writing Modular Code ##

import csv

def read_data():
    f = open("top100.csv","r")
    return list(csv.reader(f))

    
def get_data():
    stream_numbers = []
    track_names = []

    for song in music[1:]:
        stream_numbers.append(int(song[3]))
        track_names.append(song[0])
        
    return stream_numbers, track_names


dir()

## 7. Local and Global Variables ##

filename = "top100.csv"

def read_data(filename):
    f = open(filename)
    return list(csv.reader(f))

f = read_data(filename)

## 8. Using Programming Paradigms ##

def read_data(filename):
    f = open(filename)
    return list(csv.reader(f))


def get_data(data):
    list1 = []
    list2 = []
    for x in data[1:]:
        list1.append(int(x[3]))
        list2.append(x[0])
    return list1, list2

def ceil(data):
    ceiling = 0
    for x in data:
        if x > ceiling:
            ceiling = x
        else:
            ceiling
    return ceiling

def average(data):
    total = 0
    for x in data:
        total += x
    return total/len(data)

filename = "top100.csv"
music = read_data(filename)
stream_numbers, track_names = get_data(music)
average = average(stream_numbers)

## 9. Importing using an Alias ##

import statistics as s

variation = s.stdev(stream_numbers)

## 10. Importing Specific Objects ##

from statistics import mean, stdev, median

average = mean(stream_numbers)
variation = stdev(stream_numbers)
med = median(stream_numbers)