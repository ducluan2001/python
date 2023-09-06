lai = 0.009
tienGui = 5000000
soThang = int(input("Nhap so thang gui: "))
tongTien = 0
# while (soThang > 0):
#     tongTien = tienGui + (tienGui * lai)
#     tienGui = tongTien
#     soThang -= 1
# print("tienGui: ", int(tongTien))

for i in range(soThang, 0, -1):
    tongTien = tienGui + (tienGui * lai)
    tienGui = tongTien
print("tienGui: ", int(tongTien))
