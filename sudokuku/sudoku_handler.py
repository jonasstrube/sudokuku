from sudokuku.field_state import FieldState

class SudokuHandler:
    @staticmethod
    def set_number(number: int, line_index: int, column_index: int, sudoku_to_work_on: list) -> None:
        sudoku_to_work_on[line_index][column_index][0] = number

    @staticmethod
    def set_field_state(line_index: int, column_index: int, field_state: FieldState, sudoku_to_work_on: list) -> None:
        sudoku_to_work_on[line_index][column_index][2] = field_state
