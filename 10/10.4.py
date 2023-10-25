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

class Kilpailu:
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars
        self.finished = False

    def tunti_kuluu(self):
        for auto in self.cars:
            auto.kiihdyta(randint(-10,16))
            auto.kulje(1)
            if auto.odometer >= self.length:
                self.finished = True
            
    def tulosta_tilanne(self):
        for auto in self.cars:
            print(f"Rekisterinumero: {auto.registrationId}\tnopeus:{auto.speed}\thuippunopeus:{auto.maxSpeed}\tkuljettu matka:{auto.odometer}")

    def kilpailu_ohi(self):
        return self.finished

def main():
    autot = []
    for i in range(10):
        auto = Auto("ABC-" + str(i), randint(100, 201))
        autot.append(auto)
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
    hour = 0
    count = 0
    while True:
        kilpailu.tunti_kuluu()
        if kilpailu.kilpailu_ohi():
            break
        if hour == 10:
            print(f"Kilpailun tunti {(count + 1) * 10}:")
            kilpailu.tulosta_tilanne()
            print("\n")
            hour = 0
            count += 1
        else:
            hour += 1
    print(f"Kilpailun lopputulos:")
    kilpailu.tulosta_tilanne()
if __name__ == "__main__":
    main()
