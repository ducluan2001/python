# Nhập dict

thongTinSV = {}
n = 5
# nhap key va value
# for i in range(n):
#     khoa = input()
#     giatri = input()
#     thongTinSV[khoa] = giatri
# print(thongTinSV)


# nhap value
thongTinSV2 = {"ma": '', "ten": '', "tuoi": '', "dia chi": '', "hoc luc": ''}
giatriSo = ["ma", "tuoi"]

for i, txt in enumerate(thongTinSV2):
    print("Nhap", txt, ":", end="")

    if (txt == "ma" or txt == "tuoi"):
        thongTinSV2[txt] = int(input())
    else:
        thongTinSV2[txt] = input()

print(thongTinSV2)

# ep kieu trong dict
# print(int(thongTinSV2["ma"]))
