
import math

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

# cách 1
# while(a != b):
#     if(a > b):
#         a = a - b
#         # print("a",a)
#     else:
#         b = b - a
#         # print(b)
# print(a)

# cách 2
# while(a * b):
#     if(a > b):
#         a = a % b
#     else:
#         b = b % a
# print(a + b)


def x(a, b):
    if (b == 0):
        return a
    else:
        return x(b, a % b)


print(x(a, b))
