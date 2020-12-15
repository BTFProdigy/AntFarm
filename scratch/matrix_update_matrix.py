#!/bin/bash/

from contextlib import suppress
import numpy as np


def update_neighbor(matrix, num_rows, num_columns):
    current = np.array(matrix)
    # rows = num_rows
    # cols = num_columns
    # updated_matrix = [[0] * (cols - 1)] * (rows - 1)
    # right, down, left, up = None

    comp_arr = np.full(current.shape, True, dtype=bool)

    for (x, y) in np.ndenumerate(current):
        pass

    print(comp_arr)
