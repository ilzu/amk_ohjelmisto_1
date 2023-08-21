#!/bin/python3

def main():
    gender = input("Anna biologoinen sukupuolesi: ")
    hg = int(input("Anna hemoglobiiniarvosi: "))

    if gender == "mies":
        if hg < 134:
            print("Hemoglobiinisi on alhainen.")
        elif hg > 195:
            print("Hemoglobiinisi on korkea.")
        else:
            print("Hemoglobiinisi on normaali.")
    elif gender == "nainen":
        if hg < 117:
            print("Hemoglobiinisi on matala.")
        elif hg > 175:
            print("Hemoglobiinisi on korkea.")
        else:
            print("Hemoglobiinisi on normaali.")
    else:
        print("Virhe biologisen sukupuolen syötteessä.")


if __name__ == "__main__":
    main()
