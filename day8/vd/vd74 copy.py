with open('dulieusinhvien.txt', 'a') as file:
    while (True):
        maSv = input("Nhap ma sinh vien: \n")
        if (maSv == ""):
            break
        tenSv = input("Nhap ten sinh vien: \n")
        lop = input("Nhap lop sinh vien: \n")
        quequan = input("Nhap que quan sinh vien: \n")
        file.writelines([maSv, tenSv, lop, quequan])
with open('dulieusinhvien.txt', 'r') as file:
    print('\t\t'.join(["maSv", "tenSv", "lop", "quequan"]))
    r = file.readlines()
    print(r)
