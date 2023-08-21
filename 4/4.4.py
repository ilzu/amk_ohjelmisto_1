#!/bin/python3
from random import randint

def main():
    answer = randint(1,10)
    count = 0
    while True:
        count += 1
        num = int(input("Ana luku: "))
        if num < answer:
            print("Liian pieni arvaus.")
        elif num > answer:
            print("Liian suuri arvaus.")
        else:
            print("Oikein.")
            break
    print(f"Tarvitsit {count} arvausta.")

if __name__ == "__main__":
    main()

