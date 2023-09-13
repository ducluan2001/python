import math

x = float(input("Nhap x: "))
n = int(input("Nhap x: "))

s = 0

for i in range(2, 2 * n + 1, 2):
    s += math.pow(x, i)

print(s)
