# Soal 5: Stack dan Queue – Validasi Operasi

# --- STACK (LIFO: Last In First Out) ---
# Membuat stack dan menambahkan data
stack = []
stack.append('A')  # Masukkan A
stack.append('B')  # Masukkan B
stack.append('C')  # Masukkan C

# Pop dua kali (menghapus dari belakang)
stack.pop()        # Hapus C
stack.pop()        # Hapus B

# --- QUEUE (FIFO: First In First Out) ---
# Membuat queue dan menambahkan data
queue = []
queue.append('X')  # Masukkan X
queue.append('Y')  # Masukkan Y
queue.append('Z')  # Masukkan Z

# Dequeue satu kali (menghapus dari depan)
del queue[0]       # Hapus X

# --- Tampilkan hasil akhir ---
print("Stack akhir:", stack)   # Output: ['A']
print("Queue akhir:", queue)   # Output: ['Y', 'Z']