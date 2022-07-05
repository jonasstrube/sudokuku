from sudokuku import manager

class TestRemoveNumbersFromPossiblePosition:
    def test_remove_all(self):
        sudoku_input = [
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
        ]

        manager.remove_numbers_from_possible_position(line_index=3, column_index=1, sudoku=sudoku_input)

        assert sudoku_input[3][1][1] == []

    def test_remove_empty_list(self):
        sudoku_input = [
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
        ]

        manager.remove_numbers_from_possible_position(line_index=3, column_index=1, sudoku=sudoku_input, numbers_to_remove=[])

        assert set(sudoku_input[3][1][1]) == set([3, 8])

    def test_remove_list_with_1_number(self):
        sudoku_input = [
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8, 4], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [3, 8], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [4], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
            [[3, [], 2], [None, [], 0], [None, [], 0], [8, [], 2], [None, [], 0], [None, [6], 0], [4, [], 2], [1, [], 2], [None, [], 0]],
        ]

        manager.remove_numbers_from_possible_position(line_index=3, column_index=1, sudoku=sudoku_input, numbers_to_remove=[4])

        assert set(sudoku_input[3][1][1]) == set([3, 8])