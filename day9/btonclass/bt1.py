class Rectangle:
    def __init__(self, witght, height):
        self.witght = witght
        self.height = height

    def dienTichHcn(self):
        s = self.witght * self.height
        return s

    def chuViHcn(self):
        p = (self.witght + self.height) * 2
        return p


h1 = Rectangle(143, 66)

print(h1.witght)
print(h1.height)

print(h1.dienTichHcn())
print(h1.chuViHcn())
