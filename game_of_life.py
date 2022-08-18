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

def main(game_matrix):
    for i in range(0,20):
        print("generation {}".format(i))
        print(display(game_matrix))
        game_matrix = rules_for_gameoflife(game_matrix)
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