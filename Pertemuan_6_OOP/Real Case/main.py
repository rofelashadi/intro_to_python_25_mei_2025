from Manager import Manager

def main():
    list_data = [
        {
            "nama_lengkap" : "toni",
            "usia" : 30,
            "pekerjaan" : "UI & UX",
            "gaji" : 3000000,
            "jumlah_tim" : 5,
        },
        {
            "nama_lengkap" : "leo",
            "usia" : 35,
            "pekerjaan" : "Front End",
            "gaji" : 3000000,
            "jumlah_tim" : 5,
        },
        {
            "nama_lengkap" : "guruh",
            "usia" : 20,
            "pekerjaan" : "Security",
            "gaji" : 3000000,
            "jumlah_tim" : 5,
        },
    ]

    print("=====Detil Karyawan=====")
    for person in list_data:
        print("=====Profile=====")
        employee = Manager(person['nama_lengkap'],person['usia'],person['pekerjaan'],person["gaji"],person["jumlah_tim"])
        print(employee.getDetail())
        print('======detil pekerjaan=====')
        print(employee.getWork())

if __name__ == "__main__":
    main()