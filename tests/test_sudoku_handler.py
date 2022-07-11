from sudokuku.field_state import FieldState
from sudokuku.sudoku_handler import SudokuHandler

class TestSudokuHandler:
    def test_set_field_state_continuation(self):
        sudoku_input = [
                    [[3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [4, [], FieldState.FILLED], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY]],
                    [[None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [2, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [5, [], FieldState.FILLED]],
                    [[None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [3, [], FieldState.FILLED]],
                    [[6, [], FieldState.FILLED], [None, [3, 8], FieldState.EMPTY], [4, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [2, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[1, [], FieldState.FILLED], [None, [3, 8], FieldState.EMPTY], [9, [], FieldState.FILLED], [6, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [5, [], FieldState.FILLED], [4, [], FieldState.FILLED]],
                    [[None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [3, [], FieldState.FILLED], [6, [], FieldState.FILLED]],
                    [[8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [2, [], FieldState.FILLED], [7, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[None, [], FieldState.EMPTY], [9, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[7, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [3, [], FieldState.FILLED], [6, [], FieldState.FILLED], [9, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED]]
                ]
        
        assert sudoku_input[3][1][2] == FieldState.EMPTY

        SudokuHandler.set_field_state(3, 1, FieldState.BLOCKED, sudoku_input)

        assert sudoku_input[3][1][2] == FieldState.BLOCKED

        SudokuHandler.set_field_state(3, 1, FieldState.FILLED, sudoku_input)

        assert sudoku_input[3][1][2] == FieldState.FILLED

    def test_delete_possible_number(self):
        sudoku_input = [
                    [[3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [4, [], FieldState.FILLED], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY]],
                    [[None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [2, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [5, [], FieldState.FILLED]],
                    [[None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [3, [], FieldState.FILLED]],
                    [[6, [], FieldState.FILLED], [None, [3, 8], FieldState.EMPTY], [4, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [2, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[1, [], FieldState.FILLED], [None, [3, 8], FieldState.EMPTY], [9, [], FieldState.FILLED], [6, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [5, [], FieldState.FILLED], [4, [], FieldState.FILLED]],
                    [[None, [], FieldState.EMPTY], [None, [8], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [3, [], FieldState.FILLED], [6, [], FieldState.FILLED]],
                    [[8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [2, [], FieldState.FILLED], [7, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[None, [], FieldState.EMPTY], [9, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[7, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [3, [], FieldState.FILLED], [6, [], FieldState.FILLED], [9, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED]]
                ]

        assert sudoku_input[4][1][1] == [3, 8]

        SudokuHandler.delete_possible_numbers(4, 1, sudoku_input, 8)
        assert sudoku_input[4][1][1] == [3]

        SudokuHandler.delete_possible_numbers(5, 1, sudoku_input, 8)
        assert sudoku_input[5][1][1] == []

        SudokuHandler.delete_possible_numbers(6, 1, sudoku_input, 8)
        assert sudoku_input[5][1][1] == []

    def test_delete_all_possible_numbers(self):
        sudoku_input = [
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
        ]

        SudokuHandler.delete_possible_numbers(line_index=3, column_index=1, sudoku=sudoku_input)

        assert sudoku_input[3][1][1] == []

    def test_delete_possible_numbers_with_empty_list(self):
        sudoku_input = [
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
        ]

        SudokuHandler.delete_possible_numbers(line_index=3, column_index=1, sudoku=sudoku_input, numbers_to_remove=[])

        assert set(sudoku_input[3][1][1]) == set([3, 8])

    def test_delete_1_possible_number_as_list(self):
        sudoku_input = [
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8, 4], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [4], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
        ]

        SudokuHandler.delete_possible_numbers(line_index=3, column_index=1, sudoku=sudoku_input, numbers_to_remove=[4])

        assert set(sudoku_input[3][1][1]) == set([3, 8])