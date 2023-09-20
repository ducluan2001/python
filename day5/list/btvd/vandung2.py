a = []
for i in range(10):
    x = int(input("Nhap cua hang so " + str(i + 1) + " = "))
    a.append(x)
print("SX tang dan:", sorted(a))
print("dsTb:", sum(a) / len(a))
print("max:", max(a))
