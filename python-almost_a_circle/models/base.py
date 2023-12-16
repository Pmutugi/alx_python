'''this is my base class of the super class operations'''
class Base:
    '''the private class instance goes in here'''
    __nb_objects = 0
def __init__(self, id=None):
     '''initializing the none function'''
     if id == None:
        self.id = id
     else:
       '''comparing the function'''
       Base.__nb_objects +=1
       self.id = Base.__nb_objects

