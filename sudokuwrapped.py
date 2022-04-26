from array import array


class sudokuwrapped:
    def __init__(self, sudoku: array, iterations: int) -> None:
        self.sudoku = sudoku
        self.iterations = iterations