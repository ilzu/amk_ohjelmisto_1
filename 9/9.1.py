#!/bin/python3

class Auto:
    def __init__(self, registrationId, maxSpeed):
        self.registrationId = registrationId
        self.maxSpeed = maxSpeed
        self.speed = 0
        self.odometer = 0


def main():
    auto = Auto("ABC-123", 142)
    print(f"rekisterinumero: {auto.registrationId} huippunopeus: {auto.maxSpeed} nopeus: {auto.speed} kuljettu matka: {auto.odometer}")

if __name__ == "__main__":
    main()
