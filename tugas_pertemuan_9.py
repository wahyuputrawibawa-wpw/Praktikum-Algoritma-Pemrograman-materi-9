
# Soal 1 - Manipulasi List

# List kendaraan
kendaraan = ["motor", "mobil", "sepeda", "bus"]

print(f"data awal = {kendaraan}")

# a. Menambahkan 'truk' di akhir list
kendaraan.append("truk")
print(f"a. setelah ditambah truk = {kendaraan}")

# b. Menyisipkan 'becak' pada index ke-1
kendaraan.insert(1, "becak")
print(f"b. setelah disisipkan becak = {kendaraan}")

# c. Menghapus data paling belakang
kendaraan.pop()
print(f"c. setelah data terakhir dihapus = {kendaraan}")

# d. Mengubah 'sepeda' menjadi 'skuter'
kendaraan[3] = "skuter"
print(f"d. setelah sepeda diubah menjadi skuter = {kendaraan}")

# e. Menampilkan jumlah total data
jumlah_data = len(kendaraan)
print(f"e. jumlah total data = {jumlah_data}")



# Soal 2 - Operasi List

# List nilai siswa
angka = [75, 80, 90, 75, 85, 100, 65]

print(f"data nilai = {angka}")

# a. Mencari indeks skor 100
index_100 = angka.index(100)
print(f"a. indeks skor 100 = {index_100}")

# b. Menghitung jumlah siswa yang mendapat skor 75
jumlah_75 = angka.count(75)
print(f"b. jumlah siswa yang mendapat skor 75 = {jumlah_75}")

# c. Mengurutkan nilai dari terkecil hingga terbesar
angka.sort()
print(f"c. urutan nilai dari terkecil ke terbesar = {angka}")

# d. Membalik urutan nilai dari terbesar ke terkecil
angka.reverse()
print(f"d. urutan nilai dari terbesar ke terkecil = {angka}")



# Soal 3 - Menggabungkan List

menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Menggabungkan menu_tambahan ke menu_utama
menu_utama.extend(menu_tambahan)

# Menampilkan hasil gabungan
print(f"menu utama setelah digabung = {menu_utama}")



# Soal 4 - Nested List

# Data barang dan harga
data_barang = [
    ["Buku", 5000],
    ["Pensil", 2000],
    ["Penggaris", 3000]
]

# a. Menampilkan harga Pensil
harga_pensil = data_barang[1][1]

print(f"a. Harga Pensil = {harga_pensil}")

# b. Menampilkan semua data menggunakan perulangan
print("\nb. Data barang:")

for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")


