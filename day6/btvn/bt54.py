n = int(input("Nhap so luong sinh vien: "))

ds = []
tt = {"ma": '', "ten": '', "dToan": '', "dVan" : ''}

for i in range(n):
    print("Nhap thong tin sinh vien so", i+1, ":")
    for j in tt:
        print("Nhap", j, end=":")
        tt[j] = input()
    ds.append(tt.copy())
# print(ds)
sum = 0
ds2 = []
ds3 = []
print("Danh sach sinh vien")
for i in range(n):
    sum += int(ds[i]["dToan"]) + int(ds[i]["dVan"])
    ds[i]["Diem Tong"] = sum
    print("Ma",ds[i]["ma"],"|Ten",ds[i]["ten"],"|Diem Toan",ds[i]["dToan"],"|Diem Van",ds[i]["dVan"],"|Diem Tong",ds[i]["Diem Tong"])
    sum = 0
    if(int(ds[i]["Diem Tong"]) > 10 and (int(ds[i]["dToan"]) > 0 or int(ds[i]["dVan"]) > 0)):
        ds2.append(ds[i])
    if(int(ds[i]["dToan"]) <= 0 or int(ds[i]["dVan"]) <= 0):
        ds3.append(ds[i])

print("\nDanh sach sinh vien co diem tong tren 10:")
# print(len(ds2))
for i in range(len(ds2)):
    print("Ma",ds2[i]["ma"],"|Ten",ds2[i]["ten"],"|Diem Toan",ds2[i]["dToan"],"|Diem Van",ds2[i]["dVan"],"|Diem Tong ",ds2[i]["Diem Tong"])
    # print(ds2)
print("\nDanh sach sinh vien co diem liet:")
for i in range(len(ds3)):
    print("Ma",ds3[i]["ma"],"|Ten",ds3[i]["ten"],"|Diem Toan",ds3[i]["dToan"],"|Diem Van",ds3[i]["dVan"],"|Diem Tong ",ds3[i]["Diem Tong"])