n = int(input("Nhap so luong sinh vien: "))

ds = []
tt = {"ma": '', "ten": '', "lop": ''}

for i in range(n):
    print("Nhap thong tin sinh vien so", i+1, ":")
    for j in tt:
        print("Nhap", j, end=":")
        tt[j] = input()
    ds.append(tt.copy())
print(ds)
