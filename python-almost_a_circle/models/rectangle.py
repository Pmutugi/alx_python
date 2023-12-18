'''inherate the base properties using the import function'''
from models.base import Base 
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
        if width is not int:
            raise TypeError("width must be an integer")
        elif width <= 0 :
            raise ValueError("width must be > 0")
        else:
            self.__width = width  
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if height is not int:
            raise TypeError("height must be an integer")
        elif height <= 0 :
            raise ValueError("height must be > 0")
        else:
          self.__height= height
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x is not int:
            raise TypeError("x must be an integer")
        elif x < 0 :
            raise ValueError("x must be >= 0")
        else:
           self.__x= x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if y is not int:
            raise TypeError("y must be an integer")
        elif y < 0 :
            raise ValueError("y must be >= 0")
        else:
           self.__y= y

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
  
    
    

    
    