#!/bin/python3

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti = 13.2
naula = 32 * luoti
leiviska = 20 * naula

tulos = (leiviskat * leiviska + naulat * naula + luodit * luoti)
kg = int(tulos / 1000)
grams = tulos - kg

print("Massa nykymittojen mukaan: " + str(kg) + " kilogrammaa ja " + str(grams) + " grammaa.")

