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
              [0,0,1,0,1]]

    assert game_of_life.rules_for_gameoflife(game_matrix)== result
    