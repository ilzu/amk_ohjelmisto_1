#!/bin/python3

first = int(input("Anna ensimmäinen luku: "))
second = int(input("Anna toinen luku: "))
third = int(input("Anna kolmas luku: "))

_sum = first + second + third
avg = (first + second + third) / 3
product = first * second * third

print("Lukujen summa on " + str(_sum) + ", tulo on " + str(product) + " ja keskiarvo on " + str(avg))
