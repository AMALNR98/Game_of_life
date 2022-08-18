import time

def neighboring_cells(game_matrix, row, column):
    size_limit = len(game_matrix) - 1
    alive_members = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            next_row = row + i
            next_column = column + j
            if next_row == row and next_column == column:
                continue
            if next_row < 0 or next_column < 0 or next_row > size_limit or next_column > size_limit:
                continue
            if game_matrix[next_row][next_column] == 1:
                alive_members += 1
    return alive_members