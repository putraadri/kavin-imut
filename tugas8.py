 # Soal 8: Input 7 nama hari, simpan dalam tuple, tampilkan semua dan hari ke-3 & ke-5

# Langkah 1: Buat list kosong untuk menyimpan input dari user
hari_list = []

# Langkah 2: Minta input 7 hari dari pengguna
for i in range(7):
    nama_hari = input(f"Masukkan nama hari ke-{i+1}: ")
    hari_list.append(nama_hari)

# Langkah 3: Ubah list menjadi tuple agar isinya tetap (tidak bisa diubah)
hari_tuple = tuple(hari_list)

# Langkah 4: Tampilkan semua hari yang telah dimasukkan
print("\nHari-hari yang dimasukkan:")
print(hari_tuple)

# Langkah 5: Tampilkan hari ke-3 dan ke-5 (ingat: indeks dimulai dari 0)
print("Hari ke-3 adalah:", hari_tuple[2])
print("Hari ke-5 adalah:", hari_tuple[4])