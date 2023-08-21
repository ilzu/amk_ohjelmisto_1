#!/bin/python3

from random import randint

def throwDice():
    return randint(1,6)

def main():
    dice = 0
    while dice != 6:
        dice = throwDice()
        print(f"Nopan tulos oli {dice}.")

if __name__ == "__main__":
    main()
