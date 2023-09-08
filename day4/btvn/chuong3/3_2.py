import math

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

if (a == 0 and b == 0):
    print("phuong trinh co vo so nghiem")
elif (a == 0 and b != 0):
    print("phuong trinh vo nghiem")
else:
    print("phuong trinh co nghiem x = ", -b/a)
