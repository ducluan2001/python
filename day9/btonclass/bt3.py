class Circle:
    def __init__(self, r):
        self.r = r

    def chuVi(self):
        c = (self.r * 2) * 3.14
        return round(c, 2)

    def dienTich(self):
        s = self.r ** 2 * 3.14
        return s


a = Circle(int(input("Nhap r: ")))

print(a.chuVi())
print(a.dienTich())
