from sudokuku.field_status import FieldStatus

class SudokuHandler:
    @staticmethod
    def set_number(number: int, line_index: int, column_index: int, sudoku_to_work_on: list) -> None:
        sudoku_to_work_on[line_index][column_index][0] = number

    @staticmethod
    def set_field_status(line_index: int, column_index: int, field_status: FieldStatus, sudoku_to_work_on: list) -> None:
        sudoku_to_work_on[line_index][column_index][2] = field_status
