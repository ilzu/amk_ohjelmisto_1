#!/bin/python3

from random import randint

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

    def kulje(self, time):
        self.odometer += float(time) * float(self.speed)


def main():
    autot = []
    for i in range(10):
        auto = Auto("ABC-" + str(i), randint(100, 201))
        autot.append(auto)
    jatka = True
    while jatka:
        for auto in autot:
            auto.kiihdyta(randint(-10,16))
            auto.kulje(1)
        for auto in autot:
            if auto.odometer >= 10000:
                jatka = False
    for auto in autot:
        print(f"Rekisterinumero: {auto.registrationId}\tnopeus:{auto.speed}\thuippunopeus:{auto.maxSpeed}\tkuljettu matka:{auto.odometer}")

if __name__ == "__main__":
    main()
