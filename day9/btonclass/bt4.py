class Book:
    cnt = 0

    def __init__(self, tieuDe, tacGia, ISBN):
        self.tieuDe = tieuDe
        self.tacGia = tacGia
        self.ISBN = ISBN
        Book.cnt += 1

    def get_td(self):
        return self.tieuDe

    def get_tg(self):
        return self.tacGia

    def get_ISBN(self):
        return self.ISBN

    def show(self):
        print("\t\t\tTieu de: " + self.get_td(), "\n\t\t\tTac gia: " +
              self.get_tg(), "\n\t\t\tISBN: " + self.get_ISBN())

    def set_td(self, tieuDe):
        self.tieuDe = tieuDe

    def set_tg(self, tacGia):
        self.tacGia = tacGia


# print(Book.cnt)

# x1.addObject()
# print(Book.cnt)
