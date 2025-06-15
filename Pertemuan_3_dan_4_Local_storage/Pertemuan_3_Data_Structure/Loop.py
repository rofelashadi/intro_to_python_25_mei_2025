def main():
    #while
    #saat kita tahu syaratnya tapi masih ragu dengan jalan menuju syaratnya
    #check terlebih dahulu baru dijalankan

    index = 0
    print(f"====while=====")
    while index <= 1000:
        print(f"{index}. Sorry Beb !!!!!!")
        index += 1
    
    #do while
    #dikerjakan dulu baru dicheck
    # tidah ada di python


    print("=====for====")
    #for dipakai saat kamu tau syarta dan cara menujunya
    for value in range(1,10+1):
        print(f"index of {value}")

    makanan = ['daging', 'ayam', 'semangka', 'melom']
    for value in makanan:
        print(f"{value}")


#format dasar untuk memberitahukan kalau program yang dijalan pertama kali

if __name__ == "__main__": 
    main()
    
