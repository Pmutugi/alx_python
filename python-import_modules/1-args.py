import sys
def printarguments():
    arguments = sys.argv[1:]
    #check number of arguments
    num_arguments = len(arguments)
     
    output = ""
    
    #conditional statements
    if num_arguments == 0:
        output +="0 argument{}.\n".format('s' if num_arguments !=1 else "")
    else:
        output +="{} argument{}:\n".format(num_arguments,'s' if num_arguments !=1 else "")
        
    #to number our arguments
    for i, j in enumerate(arguments, 1):
        output +="{}: {}\n".format(i, j)
    return output   
if __name__== '__main__':

    print(printarguments()) 
