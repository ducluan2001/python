import math

x = int(input("Nhap so x: "))
a = int(input("Nhap so a: "))
s = 0
for i in range(1, a+1, 2):
    s += x**i
print(s)
