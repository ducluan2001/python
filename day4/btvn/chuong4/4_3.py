
import math

h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))
s = int(input("Nhap so giay: "))
k = int(input("Nhap so giay cong them: "))

s += k

while (s >= 60):
    m += 1
    s -= 60
    if (m >= 60):
        h += 1
        m -= 60
print(h, m, s)
