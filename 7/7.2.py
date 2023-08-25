#!/bin/python3

def main():    
    names = set()
    while True:
        name = input("Anna nimi: ")
        if name == "": break
        if name in names:
            print("Aiemmin syötetty nimi.")
        else:
            names.add(name)
            print("Uusi nimi.")
    for name in names:
        print(name)

if __name__ == "__main__":
    main()
