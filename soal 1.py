# Soal 1: Filter angka genap dan kalikan 2

# List awal berisi angka campuran
angka = [10, 25, 30, 17, 40, 21]

# List kosong untuk menyimpan hasil
hasil = []

# Periksa setiap angka dalam list
for a in angka:
    if a % 2 == 0:           # Jika angka genap
        hasil.append(a * 2)  # Kalikan 2 dan simpan ke hasil

# Tampilkan hasil akhir
print("Input :", angka)
print("Output:", hasil)