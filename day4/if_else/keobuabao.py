import random

keo, bua, bao = "keo", "bua", "bao"
print("1. Keo\n2. Bua\n3. Bao")

i = int(input("Ban chon: "))

r = random.randint(1, 3)

if (i >= 1 and i <= 3):
    if (i == 1 and r == 1):
        print("Ban chon %s may chon %s ---> HOÀ" % (keo, keo))
    elif (i == 1 and r == 2):
        print("Ban chon %s may chon %s ---> BẠN THUA" % (keo, bua))
    elif (i == 1 and r == 3):
        print("Ban chon %s may chon %s ---> BẠN THẮNG" % (keo, bao))
    elif (i == 2 and r == 1):
        print("Ban chon %s may chon %s ---> BẠN THẮNG" % (bua, keo))
    elif (i == 2 and r == 2):
        print("Ban chon %s may chon %s ---> HOÀ" % (bua, bua))
    elif (i == 2 and r == 3):
        print("Ban chon %s may chon %s ---> BẠN THUA" % (bua, bao))
    elif (i == 3 and r == 1):
        print("Ban chon %s may chon %s ---> BẠN THUA" % (bao, keo))
    elif (i == 3 and r == 2):
        print("Ban chon %s may chon %s ---> BẠN THẮNG" % (bao, bua))
    elif (i == 3 and r == 3):
        print("Ban chon %s may chon %s ---> HOÀ" % (bao, bao))
else:
    print("Ban chon sai vui long chon lai!")
