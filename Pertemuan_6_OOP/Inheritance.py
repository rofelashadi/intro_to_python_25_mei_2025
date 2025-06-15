#case ibu dan anak

class Ibu:
    panggilan = "Iya, Ada Apa?"
    sifat = "Lembut"

    def setSifat(self,sifat):
        self._sifat = sifat

    def getSifat(self):
        return f"Sifat dari tokoh : {self._sifat}"

    def getPanggilan(self):
        return f"{self.panggilan}"

class Anak(Ibu):
    def disuruh(self):
        return f"Nanti dulu deh!!!!"
    

#cara manggil

Toni = Anak()
Toni.panggilan = "Ton Ton"
Toni.setSifat("Pemarah")
print(Toni.getPanggilan())
print(Toni.getSifat())

