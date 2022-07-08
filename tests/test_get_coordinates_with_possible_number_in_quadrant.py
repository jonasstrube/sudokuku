import pytest

from sudokuku.field_state import FieldState
from sudokuku.manager import get_coordinates_with_possible_number_in_quadrant


class TestGetCoordinatesWithPossibleNumberInQuadrant:
    def test_third_quadrant_with_3_and_8(self):
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
        
        output = get_coordinates_with_possible_number_in_quadrant(3, 3, sudoku_input)

        assert isinstance(output, list)
        assert len(output) == 2
        assert output[0] == [3, 1]
        assert output[1] == [4, 1]