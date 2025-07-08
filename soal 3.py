# Soal 3: Set – Operasi Gabungan dan Filter Genap

# Dua set angka awal
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 1. Gabungkan kedua set (union)
hasil_union = a.union(b)

# 2. Buat set baru berisi hanya angka genap dari hasil union
genap = {x for x in hasil_union if x % 2 == 0}

# Tampilkan hasil
print("Union:", hasil_union)
print("Genap:", genap)