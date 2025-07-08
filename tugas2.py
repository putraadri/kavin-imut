# Soal 2: Dictionary – Menyimpan dan Mengakses Nilai

# 1. Membuat dictionary berisi nama dan nilai siswa
nilai_siswa = {
    "Budi": 85,
    "Ani": 78,
    "Tina": 90,
    "Joko": 65
}

# 2. Menampilkan siswa dengan nilai di atas 80
print("Siswa yang memiliki nilai di atas 80:")

for nama, nilai in nilai_siswa.items():
    if nilai > 80:
        print(nama, ":", nilai)