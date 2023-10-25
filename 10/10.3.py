#!/bin/python3

class Hissi:
    def __init__(self, bottomfloor, topfloor):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.currentfloor = bottomfloor

    def kerros_ylos(self):
        self.currentfloor += 1
        if self.currentfloor > self.topfloor: self.currentfloor = self.topfloor
        return self.currentfloor

    def kerros_alas(self):
        self.currentfloor -= 1
        if self.currentfloor < self.bottomfloor: self.currentfloor = self.bottomfloor
        return self.currentfloor

    def siirry_kerrokseen(self, floor):
        if floor == self.currentfloor: return
        if floor > self.currentfloor:
            while self.currentfloor != floor:
                self.kerros_ylos()
            return
        while self.currentfloor != floor:
            self.kerros_alas()

class Talo:
    def __init__(self, bottomfloor, topfloor, elevators):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.elevators = []
        for i in range(elevators):
            elevator = Hissi(bottomfloor, topfloor)
            self.elevators.append(elevator)

    def aja_hissia(self, hissinro, targetfloor ):
        hissi = self.elevators[hissinro]
        hissi.siirry_kerrokseen(targetfloor)

    def palohalytys(self):
        for hissi in self.elevators:
            hissi.siirry_kerrokseen(self.bottomfloor)

def main():
    talot = []
    for i in range(1, 10):
        talo = Talo(1, i, i)
        talot.append(talo)
    for talo in talot:
        print(f"talo {talot.index(talo)}:")
        for hissi in range(len(talo.elevators)) :
            print(f"hissi: {hissi}:")
            for floor in range(talo.bottomfloor, talo.topfloor +1):
                talo.aja_hissia(hissi, floor)
                print(f"Hissi on kerroksessa {talo.elevators[hissi].currentfloor}, pitäisi olla {floor}")
                talo.aja_hissia(hissi, talo.bottomfloor)
                print(f"hissi on nyt kerroksessa {talo.elevators[hissi].currentfloor}, pitäisi olla pohjakerros {talo.bottomfloor}")
        print("palohalytys!")
        talo.palohalytys()
        for hissi in talo.elevators:
            print(f"hissi {talo.elevators.index(hissi)} on kerroksessa {hissi.currentfloor}")
            
if __name__ == "__main__":
    main()
