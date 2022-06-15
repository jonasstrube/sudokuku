import pytest
from sudokuku import manager

class TestPrepareSudokuWithPrepareSudoku():
    def test_level_4_sudoku(self):
        sudoku_unsolved = [
                    [None, None, 6, 5, None, 7, 4, None, None],
                    [None, 8, None, 9, None, 3, None, 6, None],
                    [3, None, None, None, None, None, None, None, 5],
                    [7, 6, None, None, 4, None, None, 8, 2],
                    [None, None, None, 6, None, 8, None, None, None],
                    [8, 5, None, None, 9, None, None, 1, 3],
                    [5, None, None, None, None, None, None, None, 8],
                    [None, 1, None, 2, None, 9, None, 7, None],
                    [None, None, 7, 8, None, 4, 1, None, None]
                ]
        
        sudoku_solved_expected = [
                    [1, 2, 6, 5, 8, 7, 4, 3, 9],
                    [4, 8, 5, 9, 2, 3, 7, 6, 1],
                    [3, 7, 9, 4, 6, 1, 8, 2, 5],
                    [7, 6, 1, 3, 4, 5, 9, 8, 2],
                    [9, 3, 2, 6, 1, 8, 5, 4, 7],
                    [8, 5, 4, 7, 9, 2, 6, 1, 3],
                    [5, 4, 3, 1, 7, 6, 2, 9, 8],
                    [6, 1, 8, 2, 5, 9, 3, 7, 4],
                    [2, 9, 7, 8, 3, 4, 1, 5, 6]
                ]
        
        prepared_sudoku = manager.prepare_sudoku(sudoku_unsolved)
        sudoku_solved_calculated = manager.solve_sudoku(prepared_sudoku)

        assert sudoku_solved_calculated == sudoku_solved_expected

