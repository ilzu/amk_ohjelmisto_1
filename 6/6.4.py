#!/bin/python3

from random import randint

def sum(numbers):
    currentSum = 0
    for number in numbers:
        currentSum += number
    return currentSum

def main():
    numbers = []
    for i in range(randint(0, 10)):
        numbers.append(randint(0, 10))

    print(f"Lukujen {numbers} summa on {sum(numbers)}.")


if __name__ == "__main__":
    main()
