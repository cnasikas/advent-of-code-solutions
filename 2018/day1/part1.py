def main():
    sum = 0
    numbers = []

    with open('input.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for num in numbers:
        sum += num

    print(sum)


if __name__ == '__main__':
    main()
