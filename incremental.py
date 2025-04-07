class Patsient: 
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
        self.regAeg = ""

class Arst: 
    def __init__(self, nimi, vanus, eriala, aeg):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala
        self.aeg = []


class Haigla:
    patsiendiList = []
    arstideList = []

    def patsienditeKuuvamine(self):
        for index,elem in enumerate (self.patsiendiList):
            print('id: ', index, "Nimi ", elem.nimi, "Vanus ", elem.vanus)
        
    def arstideeKuuvamine(self):
        for index,elem in enumerate (self.arstideList):
            print('id: ', index, "Nimi ", elem.nimi, "Vanus ", elem.vanus, "Eriala ", elem.eriala)

    def kohtumineTegimine(self):
        patsiendiIndex = 0
        patsientiNimi = input("sisesta patsiendi nimi?");
        arstiNimi = input("sisesta arsti nimi?")
        
        for elem in arstideList:
            if elem.nimi == self.patsientiNimi:
                patsientiIndex = patsiendiList.index(elem)

        for elem in self.arstideList:
            if elem.nimi == arstNimi and len(elem.aeg) > 0:
                self.patsiendiList[patsientiIndex].regAeg = elem.aeg[0]
        for elem in self.patsiendiList:
            print("Nimi: ", elem.nimi, "Aeg: ", elem.aeg)








Patsient1 = Patsient("Thomas", 77)
Patsient2 = Patsient("Piter", 87)
Arst1 = Arst("Muhamad", 26, "allergoloog", ['10:00', '11:00', '12:00'])

haigla = Haigla()
haigla.patsiendiList.append(Patsient1)
haigla.patsiendiList.append(Patsient2)
haigla.arstideList.append(Arst1)
haigla.patsienditeKuuvamine()
haigla.arstideeKuuvamine()
haigla.kohtumineTegimine()