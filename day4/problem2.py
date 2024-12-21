#!/usr/bin/env python3

def fetch_candidate(x: int, y: int, x_term: int, y_term: int, mat: list[list[str]]) -> str:
    return mat[x][y] + mat[x + x_term][y + y_term] + mat[x + 2 * x_term][y + 2 * y_term]

def is_xmas(x: int, y: int, mat: list[list[str]], cols: int, rows: int):
    check = 0 < x < cols and 0 < y < rows
    if check:
        candidates = [fetch_candidate(x - 1, y - 1, 1, 1, mat), fetch_candidate(x + 1, y - 1, -1, 1, mat)]
        return all(canditate == 'MAS' or canditate == 'SAM' for canditate in candidates)
    return False

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

        hits = 0
        for x, row in enumerate(mat):
            for y, char in enumerate(row):
                if char == 'A' and is_xmas(x, y, mat, cols, rows):
                    hits += 1

        print(f"X-MAS: {hits}")


if __name__ == '__main__':
    main()