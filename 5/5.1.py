#!/bin/python3

from random import randint

def main():
    dices = int(input("Anna noppien lukumäärä: "))
    results = []
    for i in range(dices):
        results.append(randint(1,6))

    sum = 0
    for result in results:
        sum += result

    print(f"Noppien silmälukujen summa on {sum}")

if __name__ == "__main__":
    main()
