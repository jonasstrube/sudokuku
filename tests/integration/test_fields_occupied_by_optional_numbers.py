import pytest
from sudokuku import manager
from sudokuku.sudokuwrapped import Sudokuwrapped

class TestFieldsOccupiedByOptionalNumbers():
    def test_sudoku_with_quadrant_with_2_fields_occupied_by_2_numbers(self):
        sudoku_unsolved = [
                    [3, None, None, 8, None, None, 4, 1, None],
                    [None, 1, None, 2, 3, None, None, None, 5],
                    [None, None, 8, None, None, 1, None, None, 3],
                    [6, None, 4, None, None, None, 2, None, None],
                    [1, None, 9, 6, None, None, None, 5, 4],
                    [None, None, None, None, 8, None, None, 3, 6],
                    [8, None, None, None, 2, 7, 3, None, None],
                    [None, 9, 3, None, None, 8, None, None, None],
                    [7, None, 1, 3, 6, 9, None, None, 8]
                ]
        
        sudokuwrapped_calculated: Sudokuwrapped = manager.solve_sudoku(sudoku_unsolved)

        sudoku_solved_calculated = sudokuwrapped_calculated.sudoku

        assert sudoku_solved_calculated[4][5] == 2
        