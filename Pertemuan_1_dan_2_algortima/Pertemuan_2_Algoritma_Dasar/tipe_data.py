x = 37267
print("Ini contoh tipe data Integer : {0}".format(x))

y = 3.14
print("Ini contoh tipe data float : {0}".format(y))

z = 2 + 3j
print("Ini contoh tipe data kompleks : {0}".format(z))

#tipe data sequenc

a = [1,2,3] # list sifat tipe datanya valuenya sebisa mungkin tipe datanya sama
print("Ini contoh tipe data Integer : {0}".format(a))

b = (4,5,6) # truplet sifat tipe data tidak bisa diganti
print("Ini contoh tipe data truplet : {0}".format(b))

c = range(0,5)
print("Ini contoh tipe data range : {0}".format(c))

# text
nama = "Abdul Rachman Rofel" # tipe data string
print("Ini contoh tipe data String: {0}".format(nama))
karakter = 'A'
print("Ini contoh tipe data Integer : {0}".format(karakter))

# set
f = {1,2,3} #tipe data yang ga bisa diganti
print("Ini contoh tipe data set : {0}".format(f))

g = frozenset({4,5,6})
print("Ini contoh tipe data frozen : {0}".format(g))

#Tipe data kondisi boolean
#True (1) dan False (0)

kondisi_badan = True


#tipe data binary

i = 0b1000001
desimal = int(i)
print("Konversi binary to Desimal : {0}".format(desimal))
char = chr(desimal)
print("Ini contoh tipe data Integer : {0}".format(char))

print("Singkat binarry to char :{0}".format(chr(int(i))))

j = bytearray(a)
print("Isi binary dalam array variable a : {0}".format(j))

z = memoryview(j)
print("lokasi array dalam memory (Ram) : {0}".format(z))