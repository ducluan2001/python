n = int(input("Nhap so luong hang hoa: "))

ds = []
tt = {"ten hang": '', "so luong": '', "gia": ''}

for i in range(n):
    for j in tt:
        print("Nhap", j, end=":")
        if (j == "so luong" or j == "gia"):
            tt[j] = int(input())
        else:
            tt[j] = input()
    ds.append(tt.copy())
sum = 0
print("Danh sach hang hoa co so luong tren 50 sp: ")
for i in range(n):
    sum += ds[i]["so luong"]
    if (ds[i]["so luong"] > 50):
        print("-------", ds[i])
print("Tong so luong", sum)
