from copy import deepcopy
from sudokuku.field_state import FieldState

class SudokuHandler:
    @staticmethod
    def get_number(line_index: int, column_index: int, sudoku_to_work_on: list) -> int:
        return deepcopy(sudoku_to_work_on[line_index][column_index][0])

    @staticmethod
    def set_number(number: int, line_index: int, column_index: int, sudoku_to_work_on: list) -> None:
        sudoku_to_work_on[line_index][column_index][0] = deepcopy(number)


    @staticmethod
    def delete_possible_number(number: int, line_index: int, column_index: int, sudoku_to_work_on: list) -> list:
        possible_numbers = SudokuHandler.__get_possible_numbers(line_index, column_index, sudoku_to_work_on)
        for index in range(len(possible_numbers)):
            if possible_numbers[index] == number:
                del(sudoku_to_work_on[line_index][column_index][1][index])
                return

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
                quadrant[line][column] = __class__.__get_field(sudoku_line, sudoku_column, sudoku_to_work_on)
        
        return quadrant
    
    @staticmethod
    def prepare_sudoku(sudoku_raw: list) -> list:
        sudoku = deepcopy(sudoku_raw)
        for line in range(9):
            for column in range(9):
                if sudoku[line][column] == None:
                    sudoku[line][column] = [sudoku[line][column], [], FieldState.EMPTY]
                else:
                    sudoku[line][column] = [sudoku[line][column], [], FieldState.FILLED]
        return sudoku

    @staticmethod
    def clean_sudoku(sudoku_analytic: list) -> list:
        sudoku = deepcopy(sudoku_analytic)
        for line in range(9):
            for column in range(9):
                sudoku[line][column] = __class__.get_number(line, column, sudoku_analytic)
        return sudoku

    @staticmethod
    def __get_field(line_index: int, column_index: int, sudoku_to_work_on: list):
        return deepcopy(sudoku_to_work_on[line_index][column_index])
    
    @staticmethod
    def __get_possible_numbers(line_index: int, column_index: int, sudoku_to_work_on: list) -> list:
        return deepcopy(sudoku_to_work_on[line_index][column_index][1])
