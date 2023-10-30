#!/bin/python3

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def __str__(self):
        return f"nimi: {self.nimi}"

    def tulosta_tiedot(self):
        print(self);

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def __str__(self):
        return super().__str__() + f" kirjoittaja: {self.kirjoittaja} sivumäärä: {self.sivumaara}"

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def __str__(self):
         return super().__str__() + f" päätoimittaja: {self.paatoimittaja}"

def main():
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")

    kirja.tulosta_tiedot()
    lehti.tulosta_tiedot()
    
if __name__ == "__main__":
    main()
