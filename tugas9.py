# Soal 9: Input 5 nama buah dari pengguna, simpan dalam list, lalu ubah ke set untuk menampilkan buah unik

# Langkah 1: Buat list kosong untuk menyimpan input buah
buah_list = []

# Langkah 2: Minta input 5 buah dari pengguna
for i in range(5):
    nama_buah = input(f"Masukkan nama buah ke-{i+1}: ")
    buah_list.append(nama_buah)

# Langkah 3: Ubah list menjadi set agar hanya menyimpan buah yang unik
buah_unik = set(buah_list)

# Langkah 4: Tampilkan buah-buah unik
print("\nBuah unik yang dimasukkan:")
for buah in buah_unik:
    print(buah)