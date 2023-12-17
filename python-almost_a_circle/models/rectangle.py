'''inherate the base properties using the import function'''
Base= __import__('base').Base
'''Now create a class rectangle that inherites properties of base class imported'''
class Rectangle(Base):
    '''I will now initialize objects of the rectangle class using the init method below'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    '''We are now setting the getters and setters for each variable in our constructor'''
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, x):
        self.__width = x
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, y):
        self.__height= y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    print(y())
  
    
    

    
    