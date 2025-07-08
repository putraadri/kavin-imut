data =[1,2,2,3,4,4,5]
hasil =[]

for item in data:
    print(f"periksa item:{item}")
    if item not in hasil:
        hasil.append(item)
        print(f" {item} belum ada di hasil, tambahkan")
    else:
        print(f" {item} sudah ada di hasil, lewati")
    print("list hasil sementara:", hasil)

print("\nlist tanpa duplikat:", hasil)