import math
a = int(input("input number: "))
b = int(input("input number: "))

a, b = b, a  # đảo ngược số
print("{0}, {1}".format(a, b))

c, d, e = 5, 6, 7
print(max(c, d, e))  # in ra số lớn nhất
