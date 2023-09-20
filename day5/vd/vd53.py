l1 = []  # ds rỗng
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # ds 10 phan tu
l3 = [1, [2, 3], "bon"]  # ds chứa các phần tử khác nhau
l4 = [i for i in range(3)]  # ds tu 0 den 2
l5 = [[n, n * 1, n * 2] for n in range(1, 4)]
l6 = [x for x in range(0, 10) if x > 2 and x < 6 and x != 5]

print("l1 =", l1)
print("l2 =", l2)
print("l3 =", l3)
print("l4 =", l4)
print("l5 =", l5)
print("l6 =", l6)
