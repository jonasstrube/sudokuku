import pytest
from sudokuku import manager
from sudokuku.field_state import FieldState

class TestDetermineFieldsAndNumbersBlockedByPossibleNumbers:
    def test_2_fields_with_2_numbers(self):
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
        
        fields_to_block_by_numbers: list = manager.determine_fields_and_numbers_blocked_by_possible_numbers(number=8, quadrant_index=3, sudoku_to_work_on=sudoku_input)

        numbers = fields_to_block_by_numbers[0]
        fields = fields_to_block_by_numbers[1]

        assert set(numbers) == set([3, 8])
        assert fields[0][0] == [3, 1]
        assert fields[1][0] == [4, 1]
        assert fields[0][1] == [3, 8]
        assert fields[1][1] == [3, 8]

    def test_3_fields_with_2_numbers(self):
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
        
        fields_blocked: list = manager.determine_fields_and_numbers_blocked_by_possible_numbers(number=8, quadrant_index=3, sudoku_to_work_on=sudoku_input)

        assert fields_blocked == []
    
    def test_2_fields_with_2_numbers_but_one_fits_somewhere_else_in_quadrant(self):

        sudoku_input = [
                    [[3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [4, [], FieldState.FILLED], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY]],
                    [[None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [2, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [5, [], FieldState.FILLED]],
                    [[None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [3, [], FieldState.FILLED]],
                    [[6, [], FieldState.FILLED], [None, [3], FieldState.EMPTY], [4, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [3], FieldState.EMPTY], [2, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[1, [], FieldState.FILLED], [None, [3], FieldState.EMPTY], [9, [], FieldState.FILLED], [6, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [2, 3], FieldState.EMPTY], [None, [], FieldState.EMPTY], [5, [], FieldState.FILLED], [4, [], FieldState.FILLED]],
                    [[None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [2], FieldState.EMPTY], [None, [], FieldState.EMPTY], [3, [], FieldState.FILLED], [6, [], FieldState.FILLED]],
                    [[8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [2, [], FieldState.FILLED], [7, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[None, [], FieldState.EMPTY], [9, [], FieldState.FILLED], [3, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY]],
                    [[7, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [1, [], FieldState.FILLED], [3, [], FieldState.FILLED], [6, [], FieldState.FILLED], [9, [], FieldState.FILLED], [None, [], FieldState.EMPTY], [None, [], FieldState.EMPTY], [8, [], FieldState.FILLED]]
                ]
        
        fields_blocked: list = manager.determine_fields_and_numbers_blocked_by_possible_numbers(number=3, quadrant_index=4, sudoku_to_work_on=sudoku_input)

        assert fields_blocked == []