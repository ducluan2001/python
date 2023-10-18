class SinhVien:
    def __init__(self, hoTen, queQuan, lop, pyThon, web):
        self.hoTen = hoTen
        self.queQuan = queQuan
        self.lop = lop
        self.pyThon = pyThon
        self.web = web
    # phuong thuc (method) cua lop SinhVien

    def tinhTb(self):
        dtb = (self.pyThon * 4 + self.web * 5) / 9
        return round(dtb, 2)

    # phuong thuc (method) cua lop SinhVien
    def xepLoai(self, dtb):
        if (dtb < 5):
            print("xep loai yeu")
        elif (dtb < 7):
            print("xep loai trung binh")
        elif (dtb < 8):
            print("xep loai kha")
        elif (dtb < 9):
            print("xep loai gioi")
        else:
            print("xep loai xuat sac")

# ham khong thuoc lop SinhVien


def hocBong(dtb):
    if (dtb > 9):
        print("Hoc bong = 999999999")
    else:
        print("Hoc bong = 0")


# khoi tao gia tri cho object sv1 trong class SinhVien
sv1 = SinhVien('luan', 'bk', 'k18', 9, 10)

print(sv1.hoTen)  # truy cap thuoc tinh
print(sv1.tinhTb())  # truy cap phuong thuc tinh tb
sv1.xepLoai(sv1.tinhTb())  # truy cap phuong thuc xep loai
hocBong(sv1.tinhTb())  # ham xep loai thong qua diem tb cua doi tuong sv1
