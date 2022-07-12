# zero row and column of a zero elements of a matrix

def zero_matrix(matrix):
    first_column_zero = False
    first_row_zero = False
    # check if first row and coloumn need zeroed later
    for element in matrix[0]:
        if element == 0:
            first_row_zero = True
    for row in matrix:
        if row[0] == 0:
            first_column_zero = True

    # iterate through elements, indicate in first row and column if they need to be zeroed
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # go through rows, except first one (we will need that to 0 coloums)
    for idx in range(1, len(matrix)):
        # if element in first column is 0,
        if matrix[idx][0] == 0:
            # zero the row
            matrix[idx] = [0]*len(matrix[idx])
    for idx in range(1, len(matrix[0])):
        # if element in first row is 0,
        if matrix[0][idx] == 0:
            # zero the column
            for row in matrix:
                row[idx] = 0
    # zero first row now if needed
    if first_row_zero:
        matrix[0] = [0]*len(matrix[0])
    if first_column_zero:
        for row in matrix:
            row[0] = 0

    return matrix


if __name__ == '__main__':
    print(zero_matrix([[1, 2, 3], [4, 5, 6], [7, 0, 9], [10, 11, 12]]))
