class Shape():
    def area(self):
        sqa = self.length**(2)
        return sqa

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        sqa = self.length**(2)
        return sqa

utxt =  int(input("Enter Length of a Square: "))
obj = Square(utxt)
print("Area of Square: "+str(obj.area()))