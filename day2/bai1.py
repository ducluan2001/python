# them thu vien
import math  # thu vien toan

# ghi chu thich bang dau #

'''ghi chu thich nhieu dong 
bang dau ba dau ' '''

a = 9  # khai bao bien khong can khai bao kieu du lieu
kq = math.sqrt(a)  # can bac 2 cua a

print("Can bac 2 cua", a, "la:", math.sqrt(a))


'''làm việc với chuỗi'''
# toán tử in kiểm tra xem chuỗi con có trong chuỗi mẹ hay không

ok = "hi ma lai a"
ok1 = "hi" in ok
print(ok1)

# xu lý chuỗi
tnc = "cao dang thai nguyen"
# in cach chuoi tnc[vi tri bat dau: vi tri ket thuc: chi so buoc nhay]
print(tnc[0:8])  # in ra chuoi con
print(tnc[0:8:2])
print(tnc[::-1])  # dao nguoc chuoi

'''de xuong dong dung dau \n
-tab dung dau \t
-doi voi chuoi co the dung mot so toan tu + hoac * voi chuoi

'''
