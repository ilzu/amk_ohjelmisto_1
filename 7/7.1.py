#!/bin/python3

def main():
    seasons = ("talvi", "kevÃ¤t", "keÃ¤ä", "syksy")
    month = int(input("Anna kuukauden numero: "))

    if month > 12 or month < 1:
        print("Virheellinen kuukausi.")
        return
    
    # not as elegant way to make 12 a winter month as I would have liked,
    # but good enough.
    if month == 12:
        month = 0

    print(f"{seasons[int((month) / 3)]}")

if __name__ == "__main__":
    main()
