import math

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))

d = b**2 - 4*a*c

if (d < 0):
    print("phuong trinh vo nghiem")
elif (d == 0):
    print("Phuong trinh co nghiem kep x1 = x2 =", -b/2*a)
else:
    print("Phuong trinh co nghiem phan biet x1 = {0}, \t x2 = {1}".format(
        -b + math.sqrt(d) / 2*a, -b - math.sqrt(d) / 2*a))
