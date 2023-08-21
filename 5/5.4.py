#!/bin/python3

def main():
    cities = []
    for i in range(1, 6):
        cities.append(input("Anna kaupunki: "))
    for city in cities:
        print(f"{city}")



if __name__ == "__main__":
    main()
