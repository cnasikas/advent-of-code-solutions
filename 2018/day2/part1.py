from collections import Counter


def main():
    words = []
    counts = []
    totalWithTwoLetter = 0
    totalWithThreeLetter = 0

    with open('input.txt', 'r') as file:
        words = [line.strip() for line in file]

    for word in words:
        counts.append(Counter(word).most_common(2))

    for count in counts:
        freq = (count[0][1], count[1][1])

        if (freq[0] == 2 or freq[1] == 2):
            totalWithTwoLetter += 1

        if (freq[0] == 3 or freq[1] == 3):
            totalWithThreeLetter += 1

    print(totalWithTwoLetter * totalWithThreeLetter)


if __name__ == '__main__':
    main()
