def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1[0]) == len(m2):
        result_mul = []
        for i in range(len(m1)):
            lst = []
            for j in range(len(m2[0])):
                s = 0
                for k in range(len(m1[0])):
                    s += m1[i][k] + m2[k][j]
                lst.append(s)
            result_mul.append(lst)
        return (result_mul)
    print("Error: Matrix shapes invalid for addition")
    return None

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            l = []
            for j in range(len(m2[0])):
                l.append(m1[i][j] + m2[i][j])
            result.append(l)
        return result
    print("Error: Matrix shapes invalid for addition")
    return None


def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    line = input().split(',')
    rows = int(line[0])
    cols = int(line[1])
    mat_1 = []
    for i in range(rows):
        line = input().split(' ')
        # if len(line) == 0:
        #     print('Error: Invalid input for the matrix')
        #     return None
        if len(line) != cols:
            print('Error: Invalid input for the matrix')
            return None
        mat_1.append([int(j) for j in line])
    return mat_1

def main():
    # read matrix 1
    matrix_1 = read_matrix()
    # print(matrix_1)
    # read matrix 2
    matrix_2 = read_matrix()
    # add matrix 1 and matrix 2
    if matrix_1 != None and matrix_2 != None:
        print(add_matrix(matrix_1, matrix_2))
    # multiply matrix 1 and matrix 2
    if matrix_1 != None and matrix_2 != None:
        print(mult_matrix(matrix_1, matrix_2))
    # matrix_1 = input()
    # matrix_2 = input()
    # matrix_1 = matrix_1.split(' ')
    # matrix_2 = matrix_2.split(' ')
    # for each_index, each_str in enumerate(matrix_1):
    #     matrix_1[each_index] = each_str.split(',')
    # for each_index, each_str in enumerate(matrix_2):
    #     matrix_2[each_index] = each_str.split(',')
    # print(matrix_1, matrix_2)
if __name__ == '__main__':
    main()
