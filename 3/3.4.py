#!/bin/python3

def main():
    leap = False;
    year = int(input("Anna vuosiluku: "))
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False

    print("Vuosi " +  str(year) + str(" on karkausvuosi." if leap else " ei ole karkausvuosi."))

if __name__ == "__main__":
    main()
