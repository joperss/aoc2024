#!/usr/bin/env python3
import re

def main():
    with open("input.txt", newline='') as inputFile:
        target = inputFile.read()

        total = 0

        instructions = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", target)
        mode = "do"
        for instruction in instructions:
            operation = instruction.split("(")[0]
            if operation == "do":
                mode = "do"
            elif operation == "don't":
                mode = "don't"
            else:
                if mode == "do":
                    operands = re.findall(r"\d{1,3}", instruction)
                    total += int(operands[0]) * int(operands[1])

        print(total)

if __name__ == '__main__':
    main()