#!/bin/python3


def main():
    min = 0
    max = 0
    while True:
        inputStr = input("Ana luku: ")
        if inputStr == '': break
        num = float(inputStr)
        if num > max: max = num
        if num < min: min = num
    print(f"Syöttämistäsi luvuista suurin oli {max} ja pienin {min}")

if __name__ == "__main__":
    main()

