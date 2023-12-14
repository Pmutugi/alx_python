'''importing file rectangle from 7th file'''
Rectangle = __import__('7-rectangle').Rectangle
class Square(Rectangle):
    '''function that calculates area of the square'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size",size)
    '''function to perform string area'''
    def __str__(self):
        return "[Square] {}/{}".format(self.__size,self.__size)
    def area(self):
        return self.__size **2