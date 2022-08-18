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

def display(game_matrix):
    size = len(game_matrix)
    rows = []
    for raw in range(size):
        columns = []
        for column in range(size):
            if game_matrix[raw][column] == 1:
                columns.append("1")
            else:
                columns.append("0")
        rows.append("\t".join(columns))
    return "\n\n\n".join(rows)

def rules_gameoflife(game_matrix):
    referral_matrix = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
    rows = len(game_matrix)
    columns = len(game_matrix)
    for row in range(rows):
        for column in range(columns):
            if neighboring_cells(game_matrix, row, column) in [2, 3] and game_matrix[row][column] == 1:
                referral_matrix[row][column] = 1
            elif neighboring_cells(game_matrix, row, column) == 3 and game_matrix[row][column] == 0:
                referral_matrix[row][column] = 1
            else:
                referral_matrix[row][column] = 0
    return referral_matrix

def main(game_matrix):
    for i in range(0,20):
        print("generation {}".format(i))
        print(display(game_matrix))
        game_matrix = rules_gameoflife(game_matrix)
        flag = False
        for row in game_matrix:
            if 1 in row:
                flag = True
                break
        if not flag:
            print(f"generation {i+1}")
            print(display(game_matrix))
            break
        time.sleep(1)
if __name__ == "__main__":
    game_matrix = [[0, 0, 0, 0, 0],
                   [1, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]
    main(game_matrix)