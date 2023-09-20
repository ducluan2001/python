a = []

n = int(input("Nhap n: "))

for i in range(n):
    x = int(input("Nhap a " + str(i + 1) + " = "))
    a.append(x)
print(a)
x = int(input("Nhap x = "))
p = 0
for i in range(len(a)):
    p += a[i] * (x ** i)  # 2 * 2 ^ 0 + 3 * 2 ^ 1 + 4 * 2 ^ 2 + 5 * 2 ^ 3
print(p)
