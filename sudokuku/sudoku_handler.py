from copy import deepcopy
from sudokuku.field_state import FieldState

class SudokuHandler:
    @staticmethod
    def get_number(line_index: int, column_index: int, sudoku_to_work_on: list) -> None:
        return deepcopy(sudoku_to_work_on[line_index][column_index][0])

    @staticmethod
    def set_number(number: int, line_index: int, column_index: int, sudoku_to_work_on: list) -> None:
        sudoku_to_work_on[line_index][column_index][0] = deepcopy(number)

    @staticmethod
    def set_field_state(line_index: int, column_index: int, field_state: FieldState, sudoku_to_work_on: list) -> None:
        sudoku_to_work_on[line_index][column_index][2] = deepcopy(field_state)

    @staticmethod
    def get_quadrant(quadrant_index: int, sudoku_to_work_on: list) -> list:
        line_upper_left_field = quadrant_index - (quadrant_index % 3)
        field_upper_left_field = (quadrant_index % 3) * 3
        upper_left_field = [line_upper_left_field, field_upper_left_field]

        quadrant: list = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        for line in range(0, 3):
            for column in range(0, 3):
                sudoku_line = upper_left_field[0] + line
                sudoku_column = upper_left_field[1] + column
                # IMPORTANT fix decentralized access of blocking numbers
                quadrant[line][column] = deepcopy(sudoku_to_work_on[sudoku_line][sudoku_column])
        
        return quadrant

