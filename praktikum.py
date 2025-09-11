# 1a. Buat 3 variabel bertipe data : int float str dan list
angka = 10
teks = "nabil"
pecahan = 3.14
benar = True
daftar = [1, 2, 3, 4, 5]

#1b. tampilkan tipe datanya dengan fungsi type()
print("========================================================")
print("#1b. tampilkan tipe datanya dengan fungsi type()")
print(type(angka))
print(type(teks))
print(type(pecahan))
print(type(benar))
print(type(daftar))


# 2a. Buat list belanja (beras, minyak, dan telur).
list_belanja = ['beras' , 'minyak' , 'telur']
print("========================================================")
print("2a. Buat list belanja (beras, minyak, dan telur).")
print(list_belanja)

# 2b.Kemudian tambahkan item gula dan kopi menggunakan fungsi.
list_belanja.append('gula')
list_belanja.append('kopi')
print("========================================================")
print("2b.Kemudian tambahkan item gula dan kopi menggunakan fungsi.")
print(list_belanja)

# 2c.Tampilkan semua item dengan perulangan.
print("========================================================")
print("2c.Tampilkan semua item dengan perulangan.")
for item in list_belanja:
    print(item)


# 3a. Buat dictionary harga belanjaan:
# i. beras: 12.000
# ii. minyak: 17.000
# iii. telur: 24.000
# iv. gula:15.000
# v. kopi:20.000

harga_belanjaan = {
    'beras' : 12000,
    'minyak' : 17000,
    'telur' : 24000,
    'gula' : 15000,
    'kopi' : 20000
}
print("========================================================")
print("3a. Buat dictionary harga belanjaan:")
print(harga_belanjaan)

# 3b. Hitung dan tampilkan total harga semua belanjaan.
total_harga = sum(harga_belanjaan.values())
print("========================================================")
print("3b. Hitung dan tampilkan total harga semua belanjaan.")
print("Total harga belanjaan: Rp", total_harga)


# 4a. Buat fungsi untuk menghitung luas persegi panjang yang mengembalikan nilai luas dan keliling dari persegi panjang..
def luas_persegi(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    
    print('Luas Persegi Panjang:', luas)
    print('Keliling Persegi Panjang:', keliling)
    
    return luas, keliling

jwb_luas, jwb_keliling = luas_persegi(10, 5)

print("========================================================")
print("4a. Buat fungsi untuk menghitung luas persegi panjang yang mengembalikan nilai luas dan keliling dari persegi panjang..")
print("Luas:", jwb_luas)
print("Keliling:", jwb_keliling)


# 5. Percabangan
# a. Minta pengguna memasukkan usia, tampilkan:
# i. “Anak” jika usia 0-13
# ii. “Remaja” jika usia 14-24
# iii. “Dewasa” jika usia 25-49
# iv. “Lansia” jika usia >50
print("========================================================")
print("5. Percabangan")

usia = int(input("Masukkan usia Anda: "))
print("========================================================")
print("5. Percabangan")
if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Usia tidak valid")
    


