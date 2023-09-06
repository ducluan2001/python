
from datetime import datetime
namSinh = int(input("Nhap nam sinh: "))

year = datetime.now().year

while (namSinh < 1900 or namSinh > year):
    print("Nhap lai nam sinh: ", end=" ")
    namSinh = int(input())

print("Tuoi cua ban: ", year - namSinh)
