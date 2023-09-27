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

for txt in thongTinSV2:
    print("Nhap", txt, ":", end="")
    for x in range(len(giatriSo)):
        if (txt == giatriSo[x]):
            thongTinSV2[txt] = int(input())
            break
        else:
            thongTinSV2[txt] = input()
            break
print(thongTinSV2)

# ep kieu trong dict
# print(int(thongTinSV2["ma"]))
