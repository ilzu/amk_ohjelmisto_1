#!/bin/python3

length = float(input("Anna kuhan pituus: "))

if length  <= 37.0:
    print("Alamittainen. Laske kuha takaisin veteen kasvamaan vielä " + str(37.0 - length) + " senttiä.")
