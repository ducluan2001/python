import math

h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))
s = int(input("Nhap so giay: "))
k = int(input("Nhap so giay cong them: "))

s += k

# cách 1
while (s >= 60):
    m += 1
    s -= 60
    if (m >= 60):
        h += 1
        m -= 60

print(h, m, s)

# cách 2
sum_s = h * 3600 + m * 60 + s + k
h = int(sum_s / 3600)
m = int((sum_s % 3600) / 60)
s = sum_s - h * 3600 - m * 60
print(h, m, s)
