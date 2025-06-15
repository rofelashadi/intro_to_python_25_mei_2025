#case mobil

class Mobil:
    roda = 4 
    _warna = "default" #ini encapsulation
    __merek = "default" #merek memiliki properti protected(_ _), tidak bisa diganti di kelas apapun

    def __init__(self,brand:str = None,merek:str = None,warna:str = None): #ini konstruktor
        self.__merek = merek
        self._brand = brand
        self._warna = warna


    #method
    def getDetail(self):
        print(f"Nama brand : {self._brand}")
        print(f"Merek : {self.__merek}")
        print(f"Warna : {self.getWarna()}")
        print(f"Jumlah roda : {self.roda}")

#set and get
#set merubah nilai private
#get mengambil nilai private
    def setWarna(self,warna):
        self._warna = warna


    def getWarna(self):
        return f"{self._warna} Gross"

#cara memanggilnya

toyota = Mobil("Toyota","supra","hitam")
toyota.roda = 2 #ini pemanggilan variable public
toyota.setWarna("Merah")
toyota.getDetail()