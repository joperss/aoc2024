#!/usr/bin/env python3
import csv

list1 = []
list2 = []

with open("input.txt", newline='') as inputFile:
    reader = csv.reader(inputFile, delimiter=',')
    for row in reader:
       list1.append(row[0])
       list2.append(row[1])

list1.sort()
list2.sort()

total = 0
for x in range(0, 1000):
    distance = abs(int(list1[x]) - int(list2[x]))
    total += distance
print(total)
