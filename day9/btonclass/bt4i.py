from bt4 import Book
ds = []
# print(len(ds))

while (True):
    print("1. Show Object \n2. Them Object\n3. Xoa\n0. Thoat\n\n")
    chon = int(input("Nhap lua chon:"))
    if (chon == 0):
        break
    if (chon == 1):
        if (len(ds) == 0):
            print("Khong co sach nao")
        else:
            for i in ds:
                i.show()
    if (chon == 2):
        tieuDe = input("Nhap tieu de: ")
        tacGia = input("Nhap tac gia: ")
        ISBN = input("Nhap ISBN: ")
        ds.append(Book(tieuDe, tacGia, ISBN))
    if (chon == 3):
        ISBN = input("Nhap ISBN muon xoa: ")
        for i in ds:
            if (i.ISBN == ISBN):
                ds.remove(i)
    if (chon == 4):
        ISBN = input("Nhap ISBN muon sua: ")
        for i in ds:
            if (i.ISBN == ISBN):
                i.set_td(input("Nhap tieu de moi: "))
                i.set_tg(input("Nhap ten tac gia moi: "))
