import pytest
from sudokuku import manager
from sudokuku.sudokuwrapped import Sudokuwrapped

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
        
        sudokuwrapped_calculated: Sudokuwrapped = manager.solve_sudoku(sudoku_unsolved)

        sudoku_solved_calculated = sudokuwrapped_calculated.sudoku

        assert sudoku_solved_calculated == sudoku_solved_expected

    def test_level_6_sudoku(self):
        sudoku_unsolved = [
                    [3, None, None, 8, None, None, 4, 1, None],
                    [None, None, None, 2, 3, None, None, None, 5],
                    [None, None, 8, None, None, 1, None, None, 3],
                    [6, None, 4, None, None, None, 2, None, None],
                    [1, None, 9, 6, None, None, None, 5, None],
                    [None, None, None, None, 8, None, None, 3, 6],
                    [8, None, None, None, 2, 7, 3, None, None],
                    [None, 9, None, None, None, None, None, None, None],
                    [7, None, 1, None, 6, 9, None, None, 8]
                ]
        
        sudoku_solved_expected = [
                    [3, 6, 2, 8, 9, 5, 4, 1, 7],
                    [4, 1, 7, 2, 3, 6, 9, 8, 5],
                    [9, 5, 8, 7, 4, 1, 6, 2, 3],
                    [6, 8, 4, 1, 5, 3, 2, 7, 9],
                    [1, 3, 9, 6, 7, 2, 8, 5, 4],
                    [2, 7, 5, 9, 8, 4, 1, 3, 6],
                    [8, 4, 6, 5, 2, 7, 3, 9, 1],
                    [5, 9, 3, 4, 1, 8, 7, 6, 2],
                    [7, 2, 1, 3, 6, 9, 5, 4, 8]
                ]
        
        sudokuwrapped_calculated: Sudokuwrapped = manager.solve_sudoku(sudoku_unsolved)

        sudoku_solved_calculated = sudokuwrapped_calculated.sudoku

        assert sudoku_solved_calculated == sudoku_solved_expected

