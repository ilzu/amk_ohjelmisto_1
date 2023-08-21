#!/bin/python3


def main():
    while True:
        inches = float(input("Anna tuumamäärä: "))
        if inches < 0: break
        print(f"{inches} tuumaa on {inches * 2.54} cm.")

if __name__ == "__main__":
    main()

