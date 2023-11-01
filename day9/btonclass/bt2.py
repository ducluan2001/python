import math


class PtBac2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinhDelta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def tinhNghiem(self):
        delta = self.tinhDelta()
        if (delta < 0):
            return "Phuong trinh vo nghiem"
        elif (delta == 0):
            x = -self.b / (2 * self.a)
            return x
        else:
            x1 = round((-self.b + math.sqrt(delta)) / (2 * self.a), 2)
            x2 = round((-self.b - math.sqrt(delta)) / (2 * self.a), 2)
            return x1, x2

    def savept(self):
        with open("abc.txt", "w") as file:
            file.write(str(self.a) + "\n")
            file.write(str(self.b) + "\n")
            file.write(str(self.c) + "\n")

    def openpt():
        with open("abc.txt", 'r') as file:
            a, b, c = file.readline(), file.readline(), file.readline()
            return PtBac2(a, b, c)


def main():
    pt = None
    while (True):
        print("1. Nhap phuong trinh\n2. Doc phuong trinh tu file\n3. tinh nghiem\n4.luu phuong trinh vao file\n0. thoat")
        select = input("Moi ban chon chuc nang: ")
        if (select == "1"):
            a = float(input("Nhập hệ số a: "))
            b = float(input("Nhập hệ số b: "))
            c = float(input("Nhập hệ số c: "))
            pt = PtBac2(a, b, c)
            print("Phương trình đã được nhập thành công.")
        elif (select == "2"):
            PtBac2.openpt()
        elif select == "3":
            if pt is not None:
                kq = pt.tinhNghiem()
                print(kq)
        elif select == "4":
            if pt is not None:
                pt.savept()
                print("Phương trình đã được lưu vào file thành công.")
            else:
                print("Vui lòng nhập hoặc đọc phương trình trước.")
        else:
            break


main()


# pt1 = PtBac2(2, 4, 1)

# print(pt1.tinhDelta())

# pt1.tinhNghiem(pt1.tinhDelta())
