from Person import Person

class Employee(Person):
    def __init__(self,nama,usia,pekerjaan,gaji):
        super().__init__(nama,usia)
        self._pekerjaan = pekerjaan
        self.__gaji = gaji

    def getDetail(self):
        return f"nama Employee : {self.nama}\nUsia : {self.getUsia()}\nPekerjaan : {self._pekerjaan}\nGaji : {self.__gaji}"
    
    def getWork(self):
        return f"{self.nama} hanya seorang emplyee"