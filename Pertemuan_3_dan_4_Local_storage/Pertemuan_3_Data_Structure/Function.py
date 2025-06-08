employee = [
    {
        "nama" : "Rofel",
        "pekerjaan" : "hacker",
        "gaji" : 100000,
    },
    {
        "nama" : "Budi",
        "pekerjaan" : "IT Trainer"
    },
    {
        "nama" : "Toni",
        "pekerjaan" : "IT Trainer"
    }
]

print("===== Daftar Pekerja ========")
def detail_pekerja(nama, pekerjaan, gaji = None):
    print(f"nama : {nama}")
    print(f"pekerjaan : {pekerjaan}")
    print(f"Gaji : {gaji}")
    print(f"Pekerja yang rajin")

# cara panggil
detail_pekerja(employee[0]['nama'], employee[0]['pekerjaan'], employee[0]['gaji'])

def penjumlahan(a,b):
    return a + b

hasil_penjumlahan = penjumlahan(10,12)
print(f"hasil dari penjumlahan : {hasil_penjumlahan}")