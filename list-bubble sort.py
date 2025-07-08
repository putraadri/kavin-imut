angka =[1,2,3,4,5]
dibalik =[]

print("data awal:", angka)

for i in range(len(angka)-1,-1,1):
    print(f"ambil angka[{i}] ={angka[i]} dan tambahkan ke list'dibalik'")
    dibalik.append(angka[i])
    print("list dibalik sementara:", dibalik)
print("\n urutan dibalik:", dibalik)