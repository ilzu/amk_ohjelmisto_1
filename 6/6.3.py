#!/bin/python3

def convert(gallons):
    return gallons * 3.785

def main():
    while True:
        gallons = float(input("Anna gallonamäärä: "))
        if gallons < 0: break
        print(f"{gallons} gallonaa on {convert(gallons)} litraa.")

if __name__ == "__main__":
    main()
