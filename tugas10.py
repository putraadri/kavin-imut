# Soal 10: Program interaktif Stack/Queue

# Langkah 1: Minta user pilih mode
mode = input("Pilih mode (stack / queue): ").lower()

# Langkah 2: Siapkan list kosong sebagai tempat data
data = []

# Langkah 3: Jalankan menu interaktif
while True:
    print("\nMenu:")
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Lihat data")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    # Tambah data
    if pilihan == "1":
        item = input("Masukkan data: ")
        data.append(item)

    # Hapus data
    elif pilihan == "2":
        if not data:
            print("Data kosong!")
        else:
            if mode == "stack":
                dihapus = data.pop()  # ambil dari belakang
                print("Data dihapus (LIFO/Stack):", dihapus)
            elif mode == "queue":
                dihapus = data[0]     # ambil dari depan
                del data[0]
                print("Data dihapus (FIFO/Queue):", dihapus)
            else:
                print("Mode tidak dikenali!")

    # Lihat isi data
    elif pilihan == "3":
        print("Isi data sekarang:", data)

    # Keluar
    elif pilihan == "4":
        print("Terima kasih. Program selesai.")
        break

    # Jika pilihan tidak valid
    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")