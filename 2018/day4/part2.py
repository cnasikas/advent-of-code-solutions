import datetime
import re
from collections import defaultdict


def parseDate(line):
    return datetime.datetime.strptime(line[line.find('[') + 1:line.find(']')], '%Y-%m-%d %H:%M')


def main():
    lines = []
    calendar = defaultdict(int)

    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]

    lines.sort(key=lambda l: parseDate(l))
    for l in lines:
        date = parseDate(l)
        if 'begins shift' in l:
            id = int(re.findall(r'#\d+', l)[0][1:])
        elif 'falls asleep' in l:
            start = date
        elif 'wakes up' in l:
            for t in range(start.minute, date.minute):
                calendar[(id, t)] += 1

    best = None
    for k, v in calendar.items():
        if best is None or v > calendar[best]:
            best = k

    best_guard, best_minute = best
    print(best_guard * best_minute)


if __name__ == '__main__':
    main()
