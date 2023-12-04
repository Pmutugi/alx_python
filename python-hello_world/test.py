import random
number = random.randint(-10000, 10000)
last=-(-number%10)

if number>0:
    
 
    if  last>5 :
         print("Last digit of",number,"is",last,"and is greater than 5")
    elif last==0:
         print("Last digit of",number,"is",last,"and is 0")
    else:
         print("Last digit of",number,"is",last,"and is less than 6 and not 0")


elif number<0:
    


    if last==0:
         print("Last digit of",number,"is",last,"and is 0")
    else:
         print("Last digit of",number, "is",last, "and is 0")
         
         
def add(a, b):
    sum = a + b
    return sum 

if __name__== "__main__":
    a = 1
    b = 2
from add_0 import add
results= add(a, b)
print("{}+{}={}".format(a,b,results))


