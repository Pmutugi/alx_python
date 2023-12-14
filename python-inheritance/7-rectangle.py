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
    def __dir__(self):
        """
        Customize the dir() output to specify the order of attributes.

        Returns:
            list: A sorted list of attribute names.
        """
        return sorted(['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']) 
        
    