'''this is a square importing functionalities of a rectangle class. the import function imports all properties of this class'''
from models.rectangle import Rectangle
'''this is a square importing functionalities of a rectangle class. the import function imports all properties of this class'''
class Square(Rectangle):
    
    '''this imports the super class functionalities of the super class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=0, y=0, id=None)
        self.size=size
        self.x= x
        self.y= y
        
        
    def __str__(self):
         return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
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
   
    