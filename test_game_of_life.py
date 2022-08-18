from unittest import result
import game_of_life

def test_rules_gameoflife():
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

    assert game_of_life.rules_gameoflife(game_matrix)== result

def test_nigbours_cell():
    game_matrix = [[0,1,0],
                   [1,0,1],
                   [0,1,0]]
    assert game_of_life.neighboring_cells(game_matrix,1,1)==4
    assert game_of_life.neighboring_cells(game_matrix,0,1)==2

def test_display():
    game_matrix = [[0,1,0],
                   [1,0,1],
                   [0,1,0]]
    
    result = '0\t1\t0\n\n\n1\t0\t1\n\n\n0\t1\t0'
    assert game_of_life.display(game_matrix) == result

