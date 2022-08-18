import game_of_life

def test_rules_for_gameoflife():
    game_matrix = [[0,0,0,0,0],
                   [0,0,0,0,0],
                   [0,1,1,1,0],
                   [0,0,0,0,0],
                   [0,0,0,0,0]]
    result = [[0,0,0,0,0],
              [0,0,1,0,0],
              [0,0,1,0,0],
              [0,0,1,0,0],
              [0,0,0,0,0]]

    assert game_of_life.rules_for_gameoflife(game_matrix)== result

def test_for_nigbours_cell():
    game_matrix = [[0,1,0],
                   [1,0,1],
                   [0,1,0]]
    assert game_of_life.neighbouring_cells(game_matrix,1,1)==4
    assert game_of_life.neighbouring_cells(game_matrix,0,1)==2



