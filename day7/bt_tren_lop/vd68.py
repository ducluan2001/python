def nhapDaThuc():
    daThuc = {}

    while (True):
        mu = int(input("Mu = "))
        if (mu == -1):
            break
        heSo = float(input("He so = "))
        if (heSo != 0):
            daThuc[mu] = heSo

    return daThuc


def hienThiDT(daThuc):
    chuoiDaThuc = ""
    for mu in sorted(daThuc.keys()):
        if (daThuc[mu] > 0):
            chuoiDaThuc = chuoiDaThuc + "+" + \
                str(daThuc[mu]) + "* x^" + str(mu)
        else:
            chuoiDaThuc = chuoiDaThuc + str(daThuc[mu]) + "* x^" + str(mu)

    print("P = ", chuoiDaThuc)


def tongDT(daThuc1, daThuc2):
    daThuc = {}
    for mu in daThuc1:
        if (mu in daThuc2):
            daThuc[mu] = daThuc1[mu] + daThuc2[mu]
        else:
            daThuc[mu] = daThuc1[mu]

    for mu in daThuc2:
        if mu not in daThuc1:
            daThuc[mu] = daThuc2[mu]

    return daThuc


def giaTriDaThuc(daThuc, x):
    return sum(daThuc[mu] * (x ** mu) for mu in daThuc)


def main():
    print("Nhap da thuc 1")
    daThuc1 = nhapDaThuc()
    print("Nhap da thuc 2")
    daThuc2 = nhapDaThuc()

    print("Tong 2 da thuc")
    daThucKetQua = tongDT(daThuc1, daThuc2)
    hienThiDT(daThuc1)
    hienThiDT(daThuc2)
    hienThiDT(daThucKetQua)

    x = 1
    print("Gia tri cua da thuc 1")
    print(giaTriDaThuc(daThuc1, x))
    print("Gia tri cua da thuc 2")
    print(giaTriDaThuc(daThuc2, x))
    print("Gia tri cua da thuc 2")
    print(giaTriDaThuc(daThucKetQua, x))


main()
