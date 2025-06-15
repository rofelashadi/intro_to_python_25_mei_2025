import random #ini disebut library di pyhton kalau di java disebut package, kalo di C disebut header

def random_generate(jumlah_data):
    list_data = []
    for index in range(jumlah_data):
        value = random.randint(1,100)
        list_data.append(value)

    return list_data

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0,n-i-1):
            if data[j] > data [j+1]: #ini pengurutan ascending
                #temp = data[j]
                #data[j] = data[j+1]
                #data[j+1] = temp
                data[j],data[j+1] = data[j+1],data[j]

def selection_sort(data):
    n = len(data)
    for i in range (n):
        min_index = 1
        for j in range(i+1,n):
            if data[j] < data[min_index]:
                min_index = j
        data[i],data[min_index] = data[min_index],data[i]


def insertion_sort(data):
     for i in range(1,len(data)):
          kunci = data[i]
          j = i - 1
          while j>= 0 and kunci < data[j]:
               data[j+1] = data[j]
               j -= 1
          data[j+1] = kunci


def merge_short(data):
     if len(data) > 1:
          mid = len(data) // 2
          kiri = data[:mid]
          kanan = data[mid:]
          merge_short(kiri) #rekursif ini bahaya
          merge_short(kanan)


          i = j = k = 0
          while i < len(kiri) and j < len(kanan):
               if kiri[i] < kanan[j]:
                    data[k] = kiri[i]
                    i += 1
               else:
                    data[k] = kanan[j]
                    j += 1
               k += 1
               
          while 1 < len(kiri):
               data[k] = kiri[i]
               i += 1
               k += 1
          while j < len(kanan):
               data[k] = kanan[j]
               j += 1
               k += 1
            

def main():
    #error handling adalah teknik program agar terus berjalan
    #kiss keep it simple, stupid
    #try:
            banyak_data = int(input("Banyak data yang akan digenerate :"))
        #validation teknik untuk melakukan pengecekan lebih lanjut
        #if banyak_data <= 0:
            #print("banyak data harus lebih dari 0")
            #main()
        #else:
            list_data = random_generate(banyak_data)
            print("====List Data Random====")
            print(list_data)
            input("Please Press Enter to next step ....")  
            #bubble_sort(list_data) 
            #selection_sort(list_data)
            #insertion_sort(list_data)
            merge_short(list_data)
            print("====Data Setelah di short====")
            print(list_data) 
    #except:
        #print("Masukkan data dengan tipe numerik!!!")
        #1main()




if __name__ == "__main__":
   main()
