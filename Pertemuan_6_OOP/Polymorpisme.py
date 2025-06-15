from abc import ABC, abstractclassmethod
class Kendaraan(ABC):
    @abstractclassmethod
    def menyalakanMesin(self):
        pass

class Motor(Kendaraan):
    def menyalakanMesin(self):
        print("Status motor : mogok")

class Mobil(Kendaraan):
    def menyalakanMesin(self):
        print("Status Mobil : Kehabisan Bensin")

class Pesawat(Kendaraan):
    def menyalakanMesin(self):
        print("Status Pesawat : Jatu")

class Kereta(Kendaraan):
    def menyalakanMesin(self):
        print("Status Pesawat : Habis Batubara")

#Polumorphisme

def menyalakanMesin(Kendaraan):
    Kendaraan.menyalakanMesin()


bebek = Motor()
supra = Mobil()
boing = Pesawat()
kai = Kereta()

menyalakanMesin(bebek)
menyalakanMesin(supra)
menyalakanMesin(boing)
menyalakanMesin(kai)
