#case mobil

class Mobil:
    roda = 4 # roda disebut object yang memiliki properti public, bisa diubah diluar kelas semaunya
    _warna = "default" #warna memiliki properti private, nilainya bisa diubah jika diijinkan
    __merek = "default" #merek memiliki properti protected(_ _), tidak bisa diganti di kelas apapun

    def __init__(self,brand:str = None,merek:str = None,warna:str = None): #ini konstruktor
        self.__merek = merek
        self._brand = brand
        self._warna = warna

    #method
    def getDetail(self):
        print(f"Nama brand : {self._brand}")
        print(f"Merek : {self.__merek}")
        print(f"Warna : {self._warna}")
        print(f"Jumlah roda : {self.roda}")

#cara memanggilnya
gakJelas = Mobil() #ini contoh gak pake constructor
gakJelas.getDetail()

toyota = Mobil("Toyota","supra","hitam")
toyota.roda = 2 #ini pemanggilan variable public
toyota.getDetail()