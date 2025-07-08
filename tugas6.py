# Soal 6: List (Input) – Menambahkan dan Mengurutkan Data

# 1. Buat list kosong untuk menyimpan angka
angka = []

# 2. Minta input dari pengguna sebanyak 5 kali
for i in range(5):
    nilai = int(input(f"Masukkan angka ke-{i+1}: "))
    angka.append(nilai)  # Tambahkan ke list

# 3. Tampilkan urutan asli (sesuai input)
print("Urutan asli:", angka)

# 4. Tampilkan urutan dari kecil ke besar
print("Urutan dari kecil ke besar:", sorted(angka))