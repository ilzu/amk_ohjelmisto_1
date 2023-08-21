#!/bin/python3

def main():
    num = int(input("Anna luku: "))
    prime = True
    for i in range(1, num):
        if num % i == 0 and i != 1 and i != num:
            prime = False
    print(f"Luku {num} {'on' if prime else 'ei ole'} alkuluku")

if __name__ == "__main__":
    main()
