#!/usr/bin/env python3

def get_order(rules):
    order = dict()
    for before, after in (rule.split('|') for rule in rules):
        if order.get(before):
            item = order[before]
            suffix = item["suffix"]
            suffix.add(after)
            item["suffix"] = suffix
            order[before] = item
        else:
            order[before] = {"suffix": {after}}
    return order

def main():
    with open("input.txt", newline='') as inputFile:
        rules = []
        updates = []
        for line in (line.strip() for line in inputFile):
            if '|' in line:
                rules.append(line)
            elif line:
                updates.append(line)

        order = get_order(rules)

        total = 0
        for update in (update.split(',') for update in updates):
            prefix = set()
            correct = True
            for number in update:
                if prefix.intersection(order.get(number)["suffix"]):
                    correct = False
                    break
                else:
                    prefix.add(number)
            if correct:
                total += int(update[(len(update) - 1) // 2])

        print(f"Rules: {rules}")
        print(f"Updates: {updates}")
        print(f"Order: {order}")
        print(f"Sum: {total}")


if __name__ == '__main__':
    main()