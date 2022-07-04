import pytest

from sudokuku.field_status import FieldStatus
from sudokuku.manager import get_coordinates_with_possible_number_in_quadrant


class TestGetCoordinatesWithPossibleNumberInQuadrant:
    def test_third_quadrant_with_3_and_8(self):
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
        
        output = get_coordinates_with_possible_number_in_quadrant(3, 3, sudoku_input)

        assert len(output) == 2
        assert output[0] == [3, 1]
        assert output[1] == [4, 1]