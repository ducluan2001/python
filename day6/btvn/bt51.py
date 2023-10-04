n = int(input("Nhap n:"))
lst = []
for i in range(n):
    lst.append(int(input("Nhap phan tu {}:".format(i + 1))))
print("Phan tu lon nhat cua list:",max(lst))
print("Tong cua list:",sum(lst))
print("list sau khi duoc sort:",sorted(lst))

cnt_am = 0
cnt_duong = 0

for i in lst:
    # print(i)
    if(i >= 0):
        cnt_duong += 1
    else:
        cnt_am += 1
print("So duong trong list:", cnt_duong)
print("So am trong list:", cnt_am)