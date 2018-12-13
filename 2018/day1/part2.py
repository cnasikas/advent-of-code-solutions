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

    while not found:
        for num in numbers:
            sum += num
            if sum in freq:
                print(sum)
                found = True
                break


if __name__ == '__main__':
    main()
