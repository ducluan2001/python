n = int(input("Nhap so luong bang dia: "))

ds = []
tt = {"ten": '', "the loai": '', "so luong": '',"gia": ''}

for i in range(n):
    print("Nhap thong tin sinh bang dia", i+1, ":")
    for j in tt:
        print("Nhap", j, end=":")
        tt[j] = input()
    ds.append(tt.copy())
# print(ds)
ds2 = []
min = ds[0]["gia"]
for i in range(n):
    print("Ten", ds[i]["ten"], "|The loai", ds[i]["the loai"], "|So luong", ds[i]["so luong"], "|Gia", ds[i]["gia"])
    if(ds[i]["gia"] < min):
        min = ds[i]["gia"]
<<<<<<< HEAD
        ds2 = []
=======
>>>>>>> 7a43ad948569d0206a6f839fba43f2c19fd299f3
        ds2.append(ds[i])
if(ds2 == []):
    ds2.append(ds[0])
print(ds2)

