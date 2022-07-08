class SudokuHandler:
    @staticmethod
    def set_number(number: int, line_index: int, column_index: int, sudoku_to_work_on: list) -> None:
        sudoku_to_work_on[line_index][column_index][0] = number