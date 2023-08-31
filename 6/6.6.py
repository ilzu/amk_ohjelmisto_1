#!/bin/python3

import math

def calculate(diameter, price):
    area = math.pi * math.pow((diameter / 100) / 2, 2)
    return price / area

def main():
    unitprice = [0, 0]
    for i in range(2):
        diameter = float(input(f"Anna pizzan {i + 1} halkaisija senttimetreinÃ¤: "))
        price = float(input(f"Anna pizzan {i + 1} hinta euroina: "))
        unitprice[i] = calculate(diameter, price)
    if unitprice[0] > unitprice[1]:
        print(f"Pizzan 2 yksikkÃ¶hinta on pienemp ({unitprice[0]} vs {unitprice[1]}).")
    elif unitprice[0] < unitprice[1]:
        print(f"Pizzan 1 yksikkÃ¶hinta on pienemp ({unitprice[0]} vs {unitprice[1]}).")
    else:
        print(f"Pizzojen yksikkÃ¶hinta on sam ({unitprice[0]}).")

if __name__ == "__main__":
    main()
