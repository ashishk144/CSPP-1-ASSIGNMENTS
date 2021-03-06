'''Tic Tac Toe'''

def check_rows(matrix_row):
    store_val = []
    for _, j in enumerate(matrix_row):
        if j[0] == j[1] and j[1] == j[2]:
            store_val.append(j[0])
    if len(store_val) == 1:
        return store_val[0]
    return 0

def check_cols(matrix_col):
    store_val = []
    for i in range(1, len(matrix_col)):
        count = 0
        for j in range(len(matrix_col[i])):
            if matrix_col[j][i-1] == matrix_col[j][i]:
                count += 1
            if count == 2:
                store_val.append(matrix_col[j][i])
    if len(store_val) == 1:
        return store_val[0]
    return 0

def check_matrix(mat_check):
    count_elem = 0
    for each_list in mat_check:
        # print(each_list)
        for each_element in each_list:
            if each_element in ('x', 'o', '.'):
                count_elem += 1
    if count_elem == 9:
        return True
    return False

def check_diag(mat_diag):
    store_val = []
    for i in range(1, len(mat_diag)):
        count = 0
        for j in range(1, len(mat_diag[i])):
            if mat_diag[i][i] == mat_diag[j][j]:
                count += 1
            if count == 2:
                store_val.append(mat_diag[i][i])
    if len(store_val) == 1:
        return store_val[0]
    return 0

def main():
    '''Taking input and delivering output'''
    new_matrix = []
    correct_count = 0
    out_put = ''
    for _ in range(3):
        line = input()
        new_matrix.append(line.split(' '))
    if check_matrix(new_matrix):
        if check_rows(new_matrix):
            correct_count += 1
            out_put += check_rows(new_matrix)
        if check_cols(new_matrix):
            correct_count += 1
            out_put += check_cols(new_matrix)
        if check_diag(new_matrix):
            correct_count += 1
        # print(correct_count)
        if correct_count == 1:
            print(out_put)
        # if correct_count == 0:
        #     print('draw')
        else:
            print('invalid game')
    else:
        print('invalid input')
if __name__ == '__main__':
    main()
