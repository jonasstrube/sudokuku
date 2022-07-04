import pytest
from sudokuku import manager
from sudokuku.field_status import FieldStatus

class TestDetermineFieldsAndNumbersBlockedByPossibleNumbers:
    def test_2_fields_with_2_numbers(self):
        sudoku_input = [
                    [[3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [4, [], FieldStatus.FILLED], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY]],
                    [[None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [5, [], FieldStatus.FILLED]],
                    [[None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [3, [], FieldStatus.FILLED]],
                    [[6, [], FieldStatus.FILLED], [None, [3, 8], FieldStatus.EMPTY], [4, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[1, [], FieldStatus.FILLED], [None, [3, 8], FieldStatus.EMPTY], [9, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [5, [], FieldStatus.FILLED], [4, [], FieldStatus.FILLED]],
                    [[None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [3, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED]],
                    [[8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [7, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[None, [], FieldStatus.EMPTY], [9, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[7, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED], [9, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED]]
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
                    [[3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [4, [], FieldStatus.FILLED], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY]],
                    [[None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [5, [], FieldStatus.FILLED]],
                    [[None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [3, [], FieldStatus.FILLED]],
                    [[6, [], FieldStatus.FILLED], [None, [3, 8], FieldStatus.EMPTY], [4, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[1, [], FieldStatus.FILLED], [None, [3, 8], FieldStatus.EMPTY], [9, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [5, [], FieldStatus.FILLED], [4, [], FieldStatus.FILLED]],
                    [[None, [], FieldStatus.EMPTY], [None, [8], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [3, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED]],
                    [[8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [7, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[None, [], FieldStatus.EMPTY], [9, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[7, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED], [9, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED]]
                ]
        
        fields_blocked: list = manager.determine_fields_and_numbers_blocked_by_possible_numbers(number=8, quadrant_index=3, sudoku_to_work_on=sudoku_input)

        assert fields_blocked == []
    
    def test_2_fields_with_2_numbers_but_one_fits_somewhere_else_in_quadrant(self):

        sudoku_input = [
                    [[3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [4, [], FieldStatus.FILLED], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY]],
                    [[None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [5, [], FieldStatus.FILLED]],
                    [[None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [3, [], FieldStatus.FILLED]],
                    [[6, [], FieldStatus.FILLED], [None, [3], FieldStatus.EMPTY], [4, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [3], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[1, [], FieldStatus.FILLED], [None, [3], FieldStatus.EMPTY], [9, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [2, 3], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [5, [], FieldStatus.FILLED], [4, [], FieldStatus.FILLED]],
                    [[None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [2], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [3, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED]],
                    [[8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [7, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[None, [], FieldStatus.EMPTY], [9, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[7, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED], [9, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED]]
                ]
        
        fields_blocked: list = manager.determine_fields_and_numbers_blocked_by_possible_numbers(number=3, quadrant_index=4, sudoku_to_work_on=sudoku_input)

        assert fields_blocked == []