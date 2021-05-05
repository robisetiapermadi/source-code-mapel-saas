# fungsi menghitung bangun datar
def hitung_luas_bangun_datar(jenis, **kwargs):
  if jenis=="segitiga":
    if kwargs['alas'] and kwargs['tinggi']:
      return float((kwargs['alas']*kwargs['tinggi'])/2)
  elif jenis=="persegi":
    if kwargs['sisi']:
      return float((kwargs['sisi']*kwargs['sisi']))
  elif jenis=="persegi_panjang":
    if kwargs['panjang'] and kwargs['lebar']:
      return float((kwargs['panjang']*kwargs['lebar']))


# contoh menghitung luas segitiga
print("luas segitiga jika alas = 5 dan tinggi = 5 => ", end="")
print(hitung_luas_bangun_datar('segitiga', alas = 5, tinggi = 5 ))

# contoh menghitung luas persegi
print("luas persegi jika panjang sisi = 10 => ", end="")
print(hitung_luas_bangun_datar('persegi', sisi = 10 ))

# contoh menghitung luas persegi panjang
print("luas persegi panjang jika panjang = 5 dan lebar = 10 => ", end="")
print(hitung_luas_bangun_datar('persegi_panjang', panjang = 5, lebar = 10 ))
