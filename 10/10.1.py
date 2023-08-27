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


def main():
    hissi = Hissi(1, 15)
    for i in range(1, 16):
        hissi.siirry_kerrokseen(i)
        print(f"Hissi on kerroksessa {hissi.currentfloor}, pitäisi olla {i}")
        hissi.siirry_kerrokseen(hissi.bottomfloor)
        print(f"hissi on nyt kerroksessa {hissi.currentfloor}, pitäisi olla {hissi.bottomfloor}")

if __name__ == "__main__":
    main()
