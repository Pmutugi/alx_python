'''this is a square importing functionalities of a rectangle class. the import function imports all properties of this class'''
from models.rectangle import Rectangle
'''this is a square importing functionalities of a rectangle class. the import function imports all properties of this class'''
class Square(Rectangle):
    
    '''this imports the super class functionalities of the super class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''we import from the class rectangle here using the super method'''
        super().__init__(size, size, x, y, id)
        
        
    def __str__(self):
         return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    '''the getter for size and setter'''
    @property
    def size(self):
        return self.size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.size = value
   
        
    
    
# if __name__ == "__main__":

#     s1 = Square(5)
#     print(s1)
#     print(s1.area())
#     s1.display()

#     print("---")

#     s2 = Square(2, 2)
#     print(s2)
#     print(s2.area())
#     s2.display()

#     print("---")

#     s3 = Square(3, 1, 3)
#     print(s3)
#     print(s3.area())
#     s3.display()
   
    