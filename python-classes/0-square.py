"""this is a class of my_square.
    It does nothing hence the pass function .
"""
class Square:
    '''initializing size'''
def __init__(self, size):
    self.__size = size
    
if __name__=="__main__":
    my_square = Square(3)
    '''try and exception method'''

    print(type(my_square))
    print(my_square.__dict__)
    try:
         print(my_square.size)
    except Exception as e:
         print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)