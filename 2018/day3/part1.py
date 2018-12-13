import re
from collections import defaultdict


def parseRectangle(rect):
    return map(int, re.findall(r'-?\d+', rect))


def main():
    claims = []

    with open('input.txt', 'r') as file:
        claims = [parseRectangle(line.strip()) for line in file]

    squares = defaultdict(list)
    overlaps = {}

    for (id, left, top, width, height) in claims:
        for i in range(left, left + width):
            for j in range(top, top + height):
                if squares[(i, j)]:
                    overlaps[(i, j)] = True

                squares[(i, j)].append(id)

    print(len(overlaps))


if __name__ == '__main__':
    main()
