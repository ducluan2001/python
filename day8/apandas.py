import pandas
# nhap file
file = open('datapandas.txt', 'a')
while (True):
    maSv = input("Nhap ma sinh vien: ")
    if (maSv == ""):
        break
    tenSv = input("Nhap ten sinh vien: ")
    lop = input("Nhap lop sinh vien: ")
    quequan = input("Nhap que quan sinh vien: ")
    file.write(','.join([maSv, tenSv, lop, quequan]) + '\n')
file.close()

# doc file
file2 = pandas.read_csv('datapandas.txt', sep=',', header=None, names=[
                        'masv', 'tensv', 'lop', 'quequan'])
lop = ['1', '2']
sv = file2.query('lop in @lop')
print(sv)
