file = open('dulieusinhvien.txt', 'w')

while (True):
    maSv = input("Nhap ma sinh vien: ")
    if (maSv == ""):
        break
    tenSv = input("Nhap ten sinh vien: ")
    lop = input("Nhap lop sinh vien: ")
    quequan = input("Nhap que quan sinh vien: ")
    file.write('\t'.join([maSv, tenSv, lop, quequan]) + '\n')
file.close()
print('\t'.join(["maSv", "tenSv", "lop", "quequan"]))
file = open('dulieusinhvien.txt', 'r')
r = file.read()
print(r)
