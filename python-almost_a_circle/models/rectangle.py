'''inherate the base properties using the import function'''
# Base= __import__('base').Base
from base import Base
'''Now create a class rectangle that inherites properties of base class imported'''
class Rectangle(Base):
    '''I will now initialize objects of the rectangle class using the init method below'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    '''We are now setting the getters and setters for each variable in our constructor'''
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height= height
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x= x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y= y
if __name__=='__main__':
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
    
  
    
    

    
    