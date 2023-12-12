class my_square:
    pass
def __init__(self, size):
    """
    the __ underscore are used to make the attribute private
    this means they cannot be accessed.
    """
    self.__size = size
    
if __name__=="__main__":
    try:
         print(my_square.size)
    except Exception as e:
         print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)