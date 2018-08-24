'''Tic Tac Toe Game'''

def is_validgame(game_grid):
    x_count, o_count = 0, 0
    for each_row in game_grid:
        for each_val in each_row:
            if each_val == 'x':
                x_count += 1
            elif each_val == 'o':
                o_count += 1
            elif each_val == '.':
                pass
            else:
                return "invalid input"
    if abs(x_count - o_count) != 1:
        return "invalid game"

def horizontal_check(game_grid):
    for each_row in game_grid:
        if each_row.count(each_row[0]) == 3 and each_row[0] != '.':
            return each_row[0]
    return None

def vertical_check(game_matrix):
    mat_len = len(game_matrix)
    win_flag = game_matrix[0][0]
    win_count = 0
    for i in range(mat_len):
        if win_count == 3:
            break
        win_count = 0
        win_flag = game_matrix[0][i]
        for j in range(mat_len):
            if game_matrix[j][i] == win_flag:
                win_count += 1
            else:
                break
    if win_count == 3:
        return win_flag
    return None

def diagonal_ltor(game_grid):
    grid_len = len(game_grid)
    win_flag = game_grid[0][0]
    win_count = 0
    if win_flag != '.':
        for i in range(grid_len):
            if game_grid[i][i] == win_flag:
                win_count += 1
    if win_count == 3:
        return win_flag
    return None

def diagonal_rtol(game_grid):
    grid_len = len(game_grid)
    win_flag = game_grid[0][-1]
    win_count = 0
    if win_flag != '.':
        for i in range(grid_len):
            if game_grid[i][-i-1] == win_flag:
                win_count += 1
            else:
                break
    if win_count == 3:
        return win_flag
    return None

def play_game(game_matrix):
    return is_validgame(game_matrix) or horizontal_check(game_matrix) or \
    vertical_check(game_matrix) or diagonal_ltor(game_matrix) or\
    diagonal_rtol(game_matrix) or 'draw'

GRIDLINES = 3
MATRIX = []
for _ in range(GRIDLINES):
    MATRIX.append(input().split(' '))
print(play_game(MATRIX))
