def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    new_matrix = []

    # Iterate through each row in the original matrix
    for row in matrix:
        # Create a new row to store the squared values for the current row
        new_row = []
        # Iterate through each element in the current row and square the value
        for element in row:
            squared_value = element ** 2
            new_row.append(squared_value)
        # Add the new row to the new matrix
        new_matrix.append(new_row)

    return new_matrix

# Test the function with the given example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)