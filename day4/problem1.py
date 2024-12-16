#!/usr/bin/env python3
def main():
    with open("input.txt", newline='') as inputFile:
        mat = []
        rows = 0
        cols = 0
        for row, line in enumerate(line.strip() for line in inputFile):
            mat.append([])
            for col, char in enumerate(line):
                mat[row].append(char)
                rows = max(row, rows)
                cols = max(col, cols)

        xs = 0
        for row in mat:
            for char in row:
                if char == 'X':
                    xs += 1
        
        print(f"X: {xs}")
        

if __name__ == '__main__':
    main()