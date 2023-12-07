def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []

        # Iterate over each element in the row and square the value
        for element in row:
            squared_value = element ** 2
            result_row.append(squared_value)

        # Append the squared row to the result matrix
        result_matrix.append(result_row)

    return result_matrix