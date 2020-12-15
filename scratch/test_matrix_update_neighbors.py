from matrix_update_matrix import update_neighbor

def test_update_neighbor():
    matrix = [[1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1]]
    rows = 5
    columns = 5
    result = update_neighbor(matrix, rows, columns)

    assert result == 4
