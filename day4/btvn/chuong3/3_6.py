
masv = input("Nhap ma sv: ")
hoten = input("Nhap ten: ")
diemRL = int(input("Nhap diem ren luyen: "))

if (diemRL >= 90):
    print("Hanh kiem xuat sac")
elif (diemRL >= 80):
    print("Hanh kiem gioi")
elif (diemRL >= 65):
    print("Hanh kiem kha")
elif (diemRL >= 50):
    print("Hanh kiem trung binh")
else:
    print("Hanh kiem yeu")
