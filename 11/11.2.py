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

    def kulje(self, time):
        self.odometer += float(time) * float(self.speed)



class SahkoAuto(Auto):
    def __init__(self, registrationId, maxSpeed, batteryCapacity):
        self.batteryCapacity = batteryCapacity
        super().__init__(registrationId, maxSpeed)

class PolttomoottoriAuto(Auto):
    def __init__(self, registrationId, maxSpeed, tankCapacity):
        self.tankCapacity = tankCapacity
        super().__init__(registrationId, maxSpeed)

def main():
    sahkoAuto = SahkoAuto("ABC-15", 180, 52.5)
    polttomoottoriAuto = PolttomoottoriAuto("ACD-123", 165, 32.3)
    
    sahkoAuto.kiihdyta(100)
    polttomoottoriAuto.kiihdyta(120)
    sahkoAuto.kulje(3)
    polttomoottoriAuto.kulje(3)

    print(f"Sähköauton matkamittarilukema: {sahkoAuto.odometer}")
    print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriAuto.odometer}")


if __name__ == "__main__":
    main()
