from array import array
from copy import deepcopy


class SudokuManager:
    @staticmethod
    def hello():
        return 'hello'

    @staticmethod
    def get_quadrant(quadrant_index: int, sudoku_to_work_on: array) -> array:
        line_upper_left_field = quadrant_index - (quadrant_index % 3)
        field_upper_left_field = (quadrant_index % 3) * 3
        upper_left_field = [line_upper_left_field, field_upper_left_field]

        quadrant: array = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        for line in range(0, 3):
            for row in range(0, 3):
                sudoku_line = upper_left_field[0] + line
                sudoku_row = upper_left_field[1] + row
                quadrant[line][row] = deepcopy(sudoku_to_work_on[sudoku_line][sudoku_row])
        
        return quadrant

    @staticmethod
    def position_is_already_taken(line: int, row: int, sudoku_or_quadrant: array) -> bool:
        if sudoku_or_quadrant[line][row][0] == None:
            return False
        else:
            return True