''' Transpose a matrix using zip'''
def transpose(matrix):
    matrix_T = []
    for each_set in zip(*matrix):
        matrix_T.append([el for el in each_set])
    return matrix_T

if __name__== "__main__":
    matrix_example = [[1, 2, 3, 11],
                      [4, 5, 6, 12],
                      [7, 8, 9, 14],
                      [15, 20, 23, -14]]
    print(transpose(matrix_example))
    

