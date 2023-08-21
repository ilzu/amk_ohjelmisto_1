#!/bin/python3

import math

def calculate(diameter, price):
    area = math.pi * math.pow((diameter / 100) / 2, 2)
    return price / area

def main():
    diameter = float(input("Anna pizzan halkaisija senttimetreinä: "))
    price = float(input("Anna pizzan hinta euroina: "))
    print(f"Pizzan hinta neliömetriltä on {calculate(diameter, price)}")


if __name__ == "__main__":
    main()
