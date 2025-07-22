import math

def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))  
    prev = 0

    while prev < n and arr[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  
        
    for i in range(prev, min(step, n)):
        if arr[i] == key:
            return i

    return -1  

data = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print("Array saat ini:", data)

cari = int(input("Masukkan angka yang ingin dicari: "))


hasil = jump_search(data, cari)

if hasil != -1:
    print("Angka ditemukan di index:", hasil)
else:
    print("Angka tidak ditemukan dalam array.")