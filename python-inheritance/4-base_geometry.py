'''This is an empty class'''
class BaseGeometry:
    '''this class does nothing'''
    def area(self): 
        raise Exception("area() is not implemented")
    def __dir__(self):
        """
        Customize the dir() output to specify the order of attributes.

        Returns:
            list: A sorted list of attribute names.
        """
        return sorted ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area']
        
