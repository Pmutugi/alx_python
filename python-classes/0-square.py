class my_square:
    """this is a class of my_square.
    It does nothing hence the pass function .
    """
    pass
def __init__(self, size):
    """
    the __ underscore are used to make the attribute private
    this means they cannot be accessed.
    """
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