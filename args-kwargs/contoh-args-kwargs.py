# pembuatan fungsi
def panggil(*nama):
  print("daftar orang yang dipanggil : ")
  for orang in nama:
    print(orang)  

# pemanggilan fungsi 
panggil("robi", "setia", "permadi")



# tanpa *args
def colek(nama1, nama2, nama3):
  print("daftar orang yang dipanggil : ")
  print(nama1)
  print(nama2)
  print(nama3)

# membuat fungsi dengan parameter *args
def kirim_sms(*nomer):
  print(nomer)

# membuat fungsi dengan parameter **kwargs
def tulis_sms(**isi):
  print(isi)
  
#kirim_sms(123,888,4444)

#tulis_sms(tujuan=123, pesan="apa kabar")


# cara lain memanggil fungsi yang memakai argumen *args atau *kwargs
list_nomer = [123,888,4444]
isi_sms = {'tujuan' : 4444, 'pesan' : 'mau daftar pak'}

kirim_sms(*list_nomer)
tulis_sms(**isi_sms)


# contoh fungsi rata-rata
def rata_rata(*data):
  banyak_data = len(data)
  jumlah_data = sum(data)
  nilai_rata_rata = float(jumlah_data) / float(banyak_data)
  return nilai_rata_rata

print(rata_rata(2,4,1,2,4,1,2,3,4,5,1,8,2))


