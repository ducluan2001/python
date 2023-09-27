a = [4, 2, 6, 7, 9, 8, 1]

n = len(a)  # Tra ve do dai cua danh sach

for i in range(n // 2):
    tmp = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = tmp
    print(i)

print(a)
