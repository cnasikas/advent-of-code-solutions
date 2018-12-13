import re
from collections import defaultdict


def parseRectangle(rect):
    return map(int, re.findall(r'-?\d+', rect))


def main():
    claims = []

    with open('input.txt', 'r') as file:
        claims = [parseRectangle(line.strip()) for line in file]

    squares = defaultdict(list)
    overlaps_ids = set()
    totals_ids = set()

    for (id, left, top, width, height) in claims:
        totals_ids.add(id)
        for i in range(left, left + width):
            for j in range(top, top + height):
                if squares[(i, j)]:
                    overlaps_ids.add(id)
                    for s in squares[(i, j)]:
                        overlaps_ids.add(s)

                squares[(i, j)].append(id)

    print(totals_ids - overlaps_ids)


if __name__ == '__main__':
    main()
