# Soal 7: Input nama dan nilai, simpan dalam dictionary, tampilkan nama dengan nilai > 70

nilai_siswa = {}  # buat dictionary kosong

# Input data 3 siswa
for i in range(3):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = int(input(f"Masukkan nilai {nama}: "))
    nilai_siswa[nama] = nilai

# Tampilkan nama siswa yang nilai > 70
print("\nSiswa dengan nilai di atas 70:")
for nama, nilai in nilai_siswa.items():
    if nilai > 70:
        print(nama)