import math


class PtBac2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinhDelta(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        return delta

    def tinhNghiem(self, delta):
        if (delta < 0):
            print("Phuong trinh vo nghiem")
        elif (delta == 0):
            print("Phuong trinh co nghiem kep x1 = x2 = ", -self.b / (2 * self.a))
        else:
            print("Phuong trinh co 2 nghiem phan biet: x1 = ", round((-
                  self.b + math.sqrt(delta)) / (2 * self.a), 2), "\nx2 = ", round((-
                                                                                   self.b - math.sqrt(delta)) / (2 * self.a), 2))


pt1 = PtBac2(2, 6, 1)

print(pt1.tinhDelta())

pt1.tinhNghiem(pt1.tinhDelta())
