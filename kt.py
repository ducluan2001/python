
class PTbac2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinhdelta(self):
        return self.b**2 - 4*self.a*self.c

    def tinhNghiem(self):
        delta = self.tinhdelta()
        if delta > 0:
            x1 = (-self.b + delta**0.5) / (2*self.a)
            x2 = (-self.b - delta**0.5) / (2*self.a)
            return x1, x2
        elif delta == 0:
            x = -self.b / (2*self.a)
            return x
        else:
            return "No real roots"

    def luu(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.a} {self.b} {self.c}")

    def load_from_file(filename):
        with open(filename, 'r') as file:
            a, b, c = map(float, file.readline().split())
            return PTbac2(a, b, c)


def print_menu():
    print("1. Nhập phương trình")
    print("2. Đọc phương trình từ file")
    print("3. Tính nghiệm")
    print("4. Lưu phương trình vào file")
    print("0. Thoát")


def main():
    pt = None

    while True:
        print_menu()
        chon = int(input("Nhập lựa chọn của bạn: "))

        if chon == 1:
            a = float(input("Nhập hệ số a: "))
            b = float(input("Nhập hệ số b: "))
            c = float(input("Nhập hệ số c: "))
            pt = PTbac2(a, b, c)
            print("Phương trình đã được nhập thành công.")
        elif chon == 2:
            filename = input("Nhập tên file: ")
            pt = PTbac2.load_from_file(filename)
            print("Phương trình đã được đọc từ file thành công.")
        elif chon == 3:
            if pt is not None:
                roots = pt.tinhNghiem()
                print("Nghiệm của phương trình:", roots)
            else:
                print("nhập hoặc đọc phương trình trước.")
        elif chon == 4:
            if pt is not None:
                filename = input("Nhập tên file: ")
                pt.luu(filename)
                print("Phương trình đã được lưu vào file thành công.")
            else:
                print("Vui lòng nhập hoặc đọc phương trình trước.")
        elif chon == 0:
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
