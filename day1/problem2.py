#!/usr/bin/env python3
import csv

list1 = []
dict2 = {}

with open("input.txt", newline='') as inputFile:
    reader = csv.reader(inputFile, delimiter=',')
    for row in reader:
        v1 = int(row[0])
        v2 = int(row[1])
        list1.append(v1)
        if v2 not in dict2:
            dict2[v2] = 1
        else:
            dict2[v2] = dict2.get(v2) + 1

list1.sort()

similarity_score = 0
for x in list1:
    similarity_score += x * dict2.get(x) if x in dict2 else 0
print(similarity_score)
