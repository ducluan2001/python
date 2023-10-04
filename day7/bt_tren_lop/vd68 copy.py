# nhap da thuc

def nhapDt():
    dt = {}
    # mu : heso
    while (True):
        mu = int(input("Nhap mu: "))
        if (mu == -1):
            break
        heSo = float(input("He so: "))
        if (heSo != 0):
            dt[mu] = heSo
    return dt


def inDt(dt):
    stringDt = ""
    for mu in sorted(dt.keys()):
        stringDt += '+' + str(dt[mu]) + "*x^" + str(mu)
    print("P =", stringDt)


def gopDt(dt1, dt2):
    dtall = {}

    for mu in dt1:
        if (mu in dt2):
            dtall[mu] = dt1[mu] + dt2[mu]
        else:
            dtall[mu] = dt1[mu]
    for mu in dt2:
        if (mu not in dt1):
            dtall[mu] = dt2[mu]
    return dtall


def sumDt(dtall, x):
    return sum(dtall[mu] * (x ** mu) for mu in dtall)


def main():
    print("Nhap da thuc 1")
    daThuc1 = nhapDt()
    print("Nhap da thuc 2")
    daThuc2 = nhapDt()

    print("Tong 2 da thuc")
    daThucKetQua = gopDt(daThuc1, daThuc2)
    inDt(daThuc1)
    inDt(daThuc2)
    inDt(daThucKetQua)

    x = 1
    print("Gia tri cua da thuc 1")
    print(sumDt(daThuc1, x))
    print("Gia tri cua da thuc 2")
    print(sumDt(daThuc2, x))
    print("Gia tri cua da thuc 2")
    print(sumDt(daThucKetQua, x))


main()
