#!/bin/python3
import random
import math

def main():
    N = int(input("Anna pisteiden määrä: "))
    i = 0
    n = 0
    while i < N:
        i += 1
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        if pow(x,2) + pow(y, 2) < 1:
            n += 1
    print(f"Piin likiarvo on {4 * n / N}")

if __name__ == "__main__":
    main()

