#!/bin/python3

def main():
    count = 0
    while count < 5:
        count += 1
        username = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")
        if username == "python" and password == "rules":
            print("Tervetuloa.")
            return
    print("Pääsy evätty.")

if __name__ == "__main__":
    main()

