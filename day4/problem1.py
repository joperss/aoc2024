#!/usr/bin/env python3

def fetch_candidate(x: int, y: int, x_term: int, y_term: int, mat: list[list[str]]) -> str:
    return mat[x][y] + mat[x + x_term][y + y_term] + mat[x + 2 * x_term][y + 2 * y_term] + mat[x + 3 * x_term][y + 3 * y_term]

def fetch_candidates(x: int, y: int, mat: list[list[str]], cols: int, rows: int):
    candidates = []
    check_left = x > 2
    check_right = x < cols - 2
    check_up = y > 2
    check_down = y < rows - 2
    if check_left:
        candidates.append(fetch_candidate(x, y, -1, 0, mat))
        if check_up:
            candidates.append(fetch_candidate(x, y, -1, -1, mat))
        if check_down:
            candidates.append(fetch_candidate(x, y, -1, +1, mat))
    if check_right:
        candidates.append(fetch_candidate(x, y, +1, 0, mat))
        if check_up:
            candidates.append(fetch_candidate(x, y, +1, -1, mat))
        if check_down:
            candidates.append(fetch_candidate(x, y, +1, +1, mat))
    if check_up:
        candidates.append(fetch_candidate(x, y, 0, -1, mat))
    if check_down:
        candidates.append(fetch_candidate(x, y, 0, +1, mat))
    return candidates

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
                if char == 'X':
                    candidates = fetch_candidates(x, y, mat, cols, rows)

                    for candidate in candidates:
                        if candidate == 'XMAS':
                            hits += 1

        print(f"XMAS: {hits}")


if __name__ == '__main__':
    main()