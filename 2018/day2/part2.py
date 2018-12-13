def differByOneCharacter(x, y):
    if len(x) == len(y):
        count_diffs = 0
        for a, b in zip(x, y):
            if a != b:
                count_diffs += 1

        if (count_diffs > 1):
            return False

        return True


def removeDifferentCharacter(x, y):
    if len(x) == len(y):
        for i, (a, b) in enumerate(zip(x, y)):
            if a != b:
                return x[:i] + x[i + 1:]


def main():
    words = []

    with open('test_input_part1.txt', 'r') as file:
        words = [line.strip() for line in file]

    for i in range(0, len(words)):
        for j in range(i + 1, len(words)):
            if (differByOneCharacter(words[i], words[j])):
                print(removeDifferentCharacter(words[i], words[j]))


if __name__ == '__main__':
    main()
