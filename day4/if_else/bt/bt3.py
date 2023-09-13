
# if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):

month = int(input("Nhap thang:"))
year = int(input("Nhap nam:"))

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("Thang co 31 ngay")
elif (month == 4 or month == 6 or month == 9 or month == 11):
    print("Thang co 30 ngay")
else:
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print("Thang co 29 ngay")
    else:
        print("Thang co 28 ngay")
