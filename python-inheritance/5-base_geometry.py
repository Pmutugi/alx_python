'''This is a class that does geometry class'''
class BaseGeometry:
    '''this class checks conditionsnothing'''
    def area(self): 
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value,int):
            raise TypeError("{} must be an integer".format(name))
        
        '''value less than zero'''
        if value <=0:
            raise ValueError('{} must be greater than 0'.format(name))
        
        