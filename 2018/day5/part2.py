import string


def isOfOppositePolarity(a, b):
    if a == b:
        return False
    if a.upper() == b:
        return True
    if a.lower() == b:
        return True

    return False


def alc_reduction(line):
    buf = []

    for c in line:
        if buf and isOfOppositePolarity(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return buf


def main():
    lines = []

    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]

    polymer = lines[0].strip()
    print(min(len(alc_reduction(c for c in polymer if c.lower() != x)) for x in string.ascii_lowercase))


if __name__ == '__main__':
    main()
