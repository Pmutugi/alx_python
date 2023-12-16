'''this is my base class of the super class operations'''
class Base:
    '''the private class instance goes in here'''
    __nb_objects = 0
def __init__(self, id=None):
     if id == None:
         __nb_objects = (id)
     else:
        __nb_objects +=1

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
