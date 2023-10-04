#  tinh tong uoc so nguyen duong
def tongUoc(a=1):
    s = 0
    if (a < 0):
        a = a * -1
    for uoc in range(1, a + 1):
        if (a % uoc == 0):
            s += uoc
    return s


print(tongUoc(6))
