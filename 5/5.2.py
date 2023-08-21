#!/bin/python3

def main():
    numbers = []
    while True:
        inputStr = input("Anna luku: ")
        if inputStr == "": break
        numbers.append(float(inputStr))
    numbers.sort(reverse = True)
    for i in range(5):
        print(f"{numbers[i]}")
        
if __name__ == "__main__":
    main()
