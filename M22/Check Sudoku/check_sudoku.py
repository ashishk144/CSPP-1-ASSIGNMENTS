'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    # print(sudoku)
    # print(sudoku[0][0])
    row = []
    for each_row in sudoku:
        row = each_row.copy()
        row.sort()
        if ''.join(row) != '123456789':
            return False
    # print(sudoku)
    for i in range(9):
        list_1 = []
        for j in range(9):
            # print(j,i)
            # print(sudoku[j][i])
            list_1.append(sudoku[j][i])
        # print(list_1)
        list_1.sort()
        if ''.join(list_1) != '123456789':
            return False
    for k in range(0, 7, 3):
        # count_ofloops = 0
        # while count_ofloops < 3:
        for i in range(k, k+3):
            list_2 = []
            for col_ran in range(0, 7, 3):
                for j in range(col_ran, col_ran+3):
                    # print(sudoku[j][i])
                    list_2.append(sudoku[j][i])
            # print(list_2)
            list_2.sort()
            # print(list_2)
            if ''.join(list_2) != '123456789':
                return False
            # count_ofloops += 1
    return True


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    # print(sudoku)
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
