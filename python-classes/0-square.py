"""this is a class of my_square.
    It does nothing hence the pass function .
"""
class my_square:
    """ To initialize size.
    the __ underscore are used to make the attribute private
    this means they cannot be accessed.
    """
def __init__(self, size):
    self.__size = size
    
if __name__=="__main__":
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