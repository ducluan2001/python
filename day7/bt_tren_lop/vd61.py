# ham tinh tong

def sum(*a):  # con tro *a
    s = 0
    n = len(a)
    for i in range(n):
        s += a[i]
    return s


print(sum(1, 2, 3, 4, 2222))
