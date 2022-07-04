from sudokuku.field_status import FieldStatus
from sudokuku import manager

class TestBlockField:
    def test_normal_case(self):
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
        
        assert sudoku_input[3][1][2] == FieldStatus.EMPTY

        manager.block_field(3, 1, sudoku_input)

        assert sudoku_input[3][1][2] == FieldStatus.BLOCKED