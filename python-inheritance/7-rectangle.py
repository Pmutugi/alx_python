'''importing base geometry'''
BaseGeometry = __import__('5-base_geometry').BaseGeometry
'''This is the class of a rectangle'''
class Rectangle(BaseGeometry):
    '''initializing the class width and height'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width",width)
        self.integer_validator ("height",height)
        '''defining area function'''
    def area(self):
        '''calculate the area'''
        return self.__width * self.__height
    '''output string format'''
    def __str__(self):
        return '[Rectangle] {:d}/{:d}'.format(self.__width,self.__height)
    