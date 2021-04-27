# Implementasi fungsi map() untuk menguppercase string pada list

words = ['hati','yang','luka','tenda','biru']

wordsUppercase = list(map(lambda x: x.upper() , words))

print(wordsUppercase)

# implementasi fungsi filter() untuk mengfilter hanya bilangan ganjil 

bilangan = [0, 1, 2, 3, 5, 8, 13]
  
hasil = filter(lambda x: x % 2 != 0, bilangan)
print(list(hasil))


# impolementasi fungsi reduce() untuk menjumlahkan semua elemen pada list
from functools import reduce

numbers = [0,1,2,3,4,5]

print(reduce(lambda x,y: x+y, numbers))