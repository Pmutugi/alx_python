def print_matrix_integer(matrix):
    for row in matrix:
        for i, number in enumerate(row):
            if i == len(row) -1:
                print("{:d}".format(number))
            else:
                print("{:d}".format(number), end=' ')
if __name__=="__main__":
    
     def print_matrix_integer(matrix):
            for row in matrix:
                print(*row)
        

    
    
