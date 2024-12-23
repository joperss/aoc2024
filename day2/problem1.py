#!/usr/bin/env python3
import csv

def is_safe_asc(report):
    return all(1 <= j - i <= 3 for i, j in zip(report, report[1:]))

def is_safe_desc(report):
    return all(-1 >= j - i >= -3 for i, j in zip(report, report[1:]))

def main():
    with open("input.txt", newline='') as reports:
        reader = csv.reader(reports, delimiter=' ')

        safe_reports = 0
        for row in reader:
            report = [int(i) for i in row]
            safe = is_safe_asc(report) or is_safe_desc(report)
            safe_reports += 1 if safe else 0

        print("Safe reports: " + str(safe_reports))

if __name__ == '__main__':
    main()
