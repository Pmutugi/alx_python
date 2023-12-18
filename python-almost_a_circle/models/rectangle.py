'''inherate the base properties using the import function'''
from models.base import Base 
'''Now create a class rectangle that inherites properties of base class imported'''
class Rectangle(Base):
    '''I will now initialize objects of the rectangle class using the init method below'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    '''We are now setting the getters and setters for each variable in our constructor'''
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
         self.__height= value
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value,int):
            raise TypeError ("x must be an integer")
        elif value < 0:
            raise ValueError ("x must be >= 0")
        else:
         self.__x= value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value,int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
           self.__y= value
        '''defining area of the rectangle in the module below. the area function reads from the set functions of width and height to obtain the actual area from the private instances'''
    def area(self):
        area= self.__width * self.__height
# if __name__ == "__main__":

#     try:
#         Rectangle(10, "2")
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.width = -10
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.x = {}
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         Rectangle(10, 2, 3, -1)
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

