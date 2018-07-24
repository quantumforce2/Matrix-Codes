''' Transpose a two dimension matrix using for loop'''
def transpose(matrix):
    matrix_T = []
    for i in range(len(matrix)+1):
        t_row = []
        for row in matrix:
            t_row.append(row[i])
        matrix_T.append(t_row)
    return matrix_T

if __name__== "__main__":
    matrix_example = [[1, 2, 3, 11, -9],
                      [4, 5, 6, 12, -15],
                      [7, 8, 9, 14, 0],
                      [15, 20, 23, -14, 20]]
    print(transpose(matrix_example))
    

