from bisect import bisect_left


def binary_search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True

    return False


def main():
    sum = 0
    numbers = []
    freq = []
    found = False

    with open('input.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for num in numbers:
        sum += num
        freq.append(sum)

    freq.sort()

    while not found:
        for num in numbers:
            sum += num
            if binary_search(freq, sum):
                print(sum)
                found = True
                break


if __name__ == '__main__':
    main()
