class Rectangle:
    def __init__(self,length, width):
        self.__length = length
        self.__width = width

    def __lt__(self,other):
        return self.__length * self.__width < other.__length * other.__width

rect1 = Rectangle(10,5)
rect2 = Rectangle(20, 10)

print(rect1 < rect2)
