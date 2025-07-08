# Soal 5: Stack dan Queue – LIFO dan FIFO

# ------------------------
# STACK (LIFO - Last In First Out)
# ------------------------
stack = []  # Buat stack kosong

# Menambahkan item ke stack
stack.append("A")
stack.append("B")
stack.append("C")
print("Isi stack:", stack)

# Mengeluarkan item dari stack (LIFO: yang terakhir masuk keluar duluan)
item_stack = stack.pop()
print("Item keluar dari stack (LIFO):", item_stack)
print("Isi stack setelah pop:", stack)

# ------------------------
# QUEUE (FIFO - First In First Out)
# ------------------------
queue = []  # Buat queue kosong

# Menambahkan item ke queue
queue.append("A")
queue.append("B")
queue.append("C")
print("\nIsi queue:", queue)

# Mengeluarkan item dari queue (FIFO: yang pertama masuk keluar duluan)
item_queue = queue[0]
del queue[0]
print("Item keluar dari queue (FIFO):", item_queue)
print("Isi queue setelah keluar:", queue)