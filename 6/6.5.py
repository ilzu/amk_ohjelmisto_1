#!/bin/python3

from random import randint

def evens(numbers):
    evenNums = []
    for number in numbers:
        if number % 2 == 0 or number == 0:
            evenNums.append(number)
    return evenNums

def main():
    numbers = []
    for i in range(randint(0, 10)):
        numbers.append(randint(0, 10))

    print(f"Alkuperäiset luvut {numbers} karsitut luvut {evens(numbers)}.")


if __name__ == "__main__":
    main()
