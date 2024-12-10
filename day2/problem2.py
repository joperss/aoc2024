#!/usr/bin/env python3
import csv
import itertools
from enum import Enum

Order = Enum('Order', [('ASC', 1), ('DESC', 2)])

def is_safe_asc(report):
    return all(j - i >= 1 and j - i <=3 for i, j in zip(report, report[1:]))

def is_safe_desc(report):
    return all(j - i <= -1 and j - i >=-3 for i, j in zip(report, report[1:]))

def is_safe_dampened(report):
    for i in range(len(report)):
        dampened_report = report[:i] + report[i+1:]
        if is_safe_asc(dampened_report) or is_safe_desc(dampened_report):
            return True
    return False

with open("input.txt", newline='') as reports:
    reader = csv.reader(reports, delimiter=' ')
    
    safe_reports = 0
    for row in reader:
        report = [int(i) for i in row]
        safe = is_safe_asc(report) or is_safe_desc(report) or is_safe_dampened(report)
        safe_reports = safe_reports + 1 if safe else 0

    print("Safe reports: " + str(safe_reports))
