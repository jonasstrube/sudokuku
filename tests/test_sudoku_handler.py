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
