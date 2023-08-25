#!/bin/python3

airports = dict()

def add():
    icao = input("Anna lentoaseman ICAO koodi: ")
    name = input("Anna lentoaseman nimi: ")
    airports[icao] =  name

def show():
    icao = input("Anna lentoaseman ICAO koodi: ")
    if icao in airports:
        print(airports[icao])
    else:
        print("Antamallasi koodilla ei löydy lentokenttää.")

def printmenu():
    print(f"1\tSyötä uuden lentoaseman tiedot")
    print(f"2\tHae lentoaseman tiedot")
    print(f"x\tLopeta")

def main():
    while True:
        printmenu()
        q = input("Anna valinta: ")
        if q == "1":
            add()
        elif q == "2":
            show()
        elif q == "x":
            return
        else:
            print("Virhellinen valinta.")

if __name__ == "__main__":
    main()
