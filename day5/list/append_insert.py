a = [2, 3, 44]
a.append(12)  # thêm vào cuối danh sách 1 phần tử
a.insert(2, 42)  # thêm vào vị trí index, giá trị phần tử
print(a)

# nhập danh sách gồm số phần tử
n = 4
for i in range(n):
    print(i+1, "=", end="")
    x = int(input())
    a.append(x)
print(a)
