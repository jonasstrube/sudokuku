import pytest
from sudokuku import manager
from sudokuku.field_status import FieldStatus

class TestBlockFieldsDefinitelyBlockedByPossibleNumbers:
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
        
        coordinates_blocked: list = manager.get_coordinates_of_fields_definitely_blocked_by_possible_numbers(number=8, quadrant_index=3, sudoku_to_work_on=sudoku_input)

        assert ((coordinates_blocked[0] == [3, 1]) or (coordinates_blocked[0] == [4, 1]))
        assert ((coordinates_blocked[1] == [3, 1]) or (coordinates_blocked[1] == [4, 1]))

    def test_3_fields_with_2_numbers(self):
        sudoku_input = [
                    [[3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [4, [], FieldStatus.FILLED], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY]],
                    [[None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [5, [], FieldStatus.FILLED]],
                    [[None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [3, [], FieldStatus.FILLED]],
                    [[6, [], FieldStatus.FILLED], [None, [3, 8], FieldStatus.EMPTY], [4, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[1, [], FieldStatus.FILLED], [None, [3, 8], FieldStatus.EMPTY], [9, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [5, [], FieldStatus.FILLED], [4, [], FieldStatus.FILLED]],
                    [[None, [], FieldStatus.EMPTY], [None, [8], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [3, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED]],
                    [[8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [2, [], FieldStatus.FILLED], [7, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[None, [], FieldStatus.EMPTY], [9, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY]],
                    [[7, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [1, [], FieldStatus.FILLED], [3, [], FieldStatus.FILLED], [6, [], FieldStatus.FILLED], [9, [], FieldStatus.FILLED], [None, [], FieldStatus.EMPTY], [None, [], FieldStatus.EMPTY], [8, [], FieldStatus.FILLED]]
                ]
        
        fields_blocked: list = manager.get_coordinates_of_fields_definitely_blocked_by_possible_numbers(number=8, quadrant_index=3, sudoku_to_work_on=sudoku_input)

        assert fields_blocked == []