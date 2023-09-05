# gán giá trị
# vd 2.41
import random as rr
import math as mt
a, b, c = 7, 5, 32
print("a = %d,b = %d,c = %d" % (a, b, c))

# vd 2.42
x = 5.1
y = (2 * x**2 + 7 * x - 2 * x)/(x + 3)
print("y = ", y)
# vd 2.43
y2 = "(2 * x**2 + 18 * x - 2 * x)/(x + 3)"
y2 = eval(y2)
print("y2 = ", y2)

# vd 2.45
s = input("Moi ban nhap vao mot chuoi: ")
print("chuoi ban vua nhap la: ", s)
print("kieu du lieu cua s la: ", type(s))
# vd 2.46
so_int = int(input("Nhap so nguyen: "))
so_float = float(input("Nhap so thuc: "))

sum = so_int + so_float
print("sum int + float = ", sum)
print("type of int + float = ", type(sum))

i = rr.randint(1, 99)
print("i = ", i)
