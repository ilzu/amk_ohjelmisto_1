#!/bin/python3

class Auto:
    def __init__(self, registrationId, maxSpeed):
        self.registrationId = registrationId
        self.maxSpeed = maxSpeed
        self.speed = 0
        self.odometer = 0


    def kiihdyta(self, speedchange):
        self.speed += float(speedchange)
        if self.speed > self.maxSpeed: self.speed = self.maxSpeed
        if self.speed < 0: self.speed = 0


def main():
    auto = Auto("ABC-123", 142)
    print(f"rekisterinumero: {auto.registrationId} huippunopeus: {auto.maxSpeed} nopeus: {auto.speed} kuljettu matka: {auto.odometer}")
    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)
    print(f"auton nopeus: {auto.speed}")
    auto.kiihdyta(-200)
    print(f"auton nopeus: {auto.speed}")

if __name__ == "__main__":
    main()
