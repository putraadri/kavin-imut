# Soal 4: Dictionary – Rekap Nilai Mahasiswa

# Dictionary berisi nama dan nilai mahasiswa
nilai = {
    "Andi": 80,
    "Budi": 70,
    "Citra": 90,
    "Dina": 60
}

# List untuk menyimpan nama yang nilainya >= 75
lulus = []

# Variabel untuk menghitung total nilai
total_nilai = 0

# Iterasi semua data
for nama, skor in nilai.items():
    total_nilai += skor  # tambahkan ke total
    if skor >= 75:
        lulus.append(nama)  # simpan nama yang lulus

# Hitung rata-rata
rata_rata = total_nilai / len(nilai)

# Tampilkan hasil
print("Lulus:", lulus)
print("Rata-rata:", rata_rata)