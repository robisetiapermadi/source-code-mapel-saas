from prettytable import PrettyTable

def tampilBarang(barang):
	print("{:^50}".format("Daftar Alat yang disewakan"))
	print("{:^50}".format("=========================="))
	daftar = PrettyTable()
	daftar.field_names = ["Kode Barang","Nama Alat", "Harga Satuan/malam"]
	daftar.align["Nama Alat"] = "l"
	for i in range(len(barang)):
		daftar.add_row([barang[i]["kode"], barang[i]["nama"], barang[i]["harga"]])
	print(daftar)

def pilihBarang():
	sewa = []
	while True:	
		#input kode barang
		while True:
			tmp_kode = input("Masukan Kode Barang : ")
			tmp_kode = tmp_kode.lower()
			for j in range(len(barang)):
				ada=False
				if tmp_kode == barang[j]["kode"]:
					ada=True
					break
			if ada==True:
				break
			else:
				print("Kode barang {} tidak ada".format(tmp_kode))

		#input jumlah barang
		while True:
			try:
				tmp_jum = int(input("Jumlah yang disewa : "))
				if tmp_jum>0 :
					break
				else:
					print("Jumlah Tidak valid, Masukan lagi !!")
			except:
				print('Isi dengan angka Bulat !!')
		while True:
			try:
				tmp_malam = int(input("Berapa lama (malam) : "))
				if tmp_malam>0 :
					break
				else:
					print("Jumlah Tidak valid, Masukan lagi !!")
			except:
				print('Isi dengan angka Bulat !!')

		#memasukan ke variabel sewa		
		sewa.append({"kode":tmp_kode, "jumlah":tmp_jum, "malam":tmp_malam})
		while True:	
			ulang = input("Tambah barang (y/t) : ") 
			ulang = ulang.lower()
			if ulang=="y" or ulang=="t":
				break
		if ulang=="t":
			break	
	return sewa

def hitung(sewa):
	total = 0
	for i in range(len(sewa)):
		for k in range(len(barang)):
			if sewa[i]["kode"]==barang[k]["kode"]:
				sewa[i]["nama"] = barang[k]["nama"]
				sewa[i]["harga"] = barang[k]["harga"]
		sewa[i]["total"] = sewa[i]["harga"] * sewa[i]["jumlah"] * sewa[i]["malam"]
		total += sewa[i]["total"]
	return sewa, total

def printStruk(x,total):
	print("{:^70}".format("Detail Pembayaran"))
	print("{:^70}".format("================="))
	struk = PrettyTable()
	struk.field_names = ["Kode Barang","Nama Alat", "Harga Satuan/malam","Jumlah alat", "Lama Sewa" , "Total" ]
	struk.align["Nama Alat"] = "l"
	for barang in x :
		struk.add_row([barang["kode"],barang["nama"],barang["harga"],barang["jumlah"],barang["malam"],barang["total"]])
	print(struk)
	print("Yang harus dibayar : {}".format(total))


def pembayaran(yang_harus_dibayar):
	while True:
		try:
			bayar = int(input("Jumlah yang dibayar : "))
			if bayar>0:
				if bayar < yang_harus_dibayar :
					print("Yang harus dibayar : {}".format(yang_harus_dibayar))
					print("Pembayaran kurang !")
				else :
					print("Kembalian : {}".format(bayar-yang_harus_dibayar))
					break
			else:
				print("Yang harus dibayar : {}".format(yang_harus_dibayar))
				print("Jumlah Tidak valid, Masukan lagi !!")
		except:
			print("Yang harus dibayar : {}".format(yang_harus_dibayar))
			print('Isi dengan angka Bulat !!')


# Deklarasi barang yang dijual
barang = [{"nama": "Tenda", "kode": "a", "harga": 35000},
          {"nama": "Sleeping Bag", "kode": "b", "harga": 7000},
          {"nama": "Carier", "kode": "c", "harga": 15000},
          {"nama": "Headlamp", "kode": "d", "harga": 5000},
          {"nama": "Matras", "kode": "e", "harga": 3000}
]

tampilBarang(barang)
sewa, total = hitung(pilihBarang())
printStruk(sewa, total)
pembayaran(total)
