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
        hits = 0
        for x, row in enumerate(mat):
            for y, char in enumerate(row):
                if char == 'X':
                    xs += 1

                    check_left = x > 2
                    check_right = x < cols - 2
                    check_up = y > 2
                    check_down = y < rows - 2

                    if check_left:
                        if mat[x - 1][y] == 'M':
                            if mat[x - 2][y] == 'A':
                                if mat[x - 3][y] == 'S':
                                    hits += 1

                        if check_up:
                            if mat[x - 1][y - 1] == 'M':
                                if mat[x - 2][y - 2] == 'A':
                                    if mat[x - 3][y - 3] == 'S':
                                        hits += 1

                        if check_down:
                            if mat[x - 1][y + 1] == 'M':
                                if mat[x - 2][y + 2] == 'A':
                                    if mat[x - 3][y + 3] == 'S':
                                        hits += 1

                    if check_right:
                        if mat[x + 1][y] == 'M':
                            if mat[x + 2][y] == 'A':
                                if mat[x + 3][y] == 'S':
                                    hits += 1

                        if check_up:
                            if mat[x + 1][y - 1] == 'M':
                                if mat[x + 2][y - 2] == 'A':
                                    if mat[x + 3][y - 3] == 'S':
                                        hits += 1

                        if check_down:
                            if mat[x + 1][y + 1] == 'M':
                                if mat[x + 2][y + 2] == 'A':
                                    if mat[x + 3][y + 3] == 'S':
                                        hits += 1

                    if check_up:
                        if mat[x][y - 1] == 'M':
                            if mat[x][y - 2] == 'A':
                                if mat[x][y - 3] == 'S':
                                    hits += 1

                    if check_down:
                        if mat[x][y + 1] == 'M':
                            if mat[x][y + 2] == 'A':
                                if mat[x][y + 3] == 'S':
                                    hits += 1


        print(f"X: {xs}")
        print(f"XMAS: {hits}")


if __name__ == '__main__':
    main()