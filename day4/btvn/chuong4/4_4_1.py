
import math

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

while(a != b):
    if(a > b):
        a = a - b
        # print("a",a)
    else:
        b = b - a
        # print(b)

print(a)