#!/bin/python3

from random import randint

def throwDice(max):
    return randint(1,int(max))

def main():
    dicemax = int(input("Anna nopan tahkoluku: "))
    dice = 0
    while dice != dicemax:
        dice = throwDice(dicemax)
        print(f"Nopan tulos oli {dice}.")

if __name__ == "__main__":
    main()
