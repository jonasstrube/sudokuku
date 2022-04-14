from array import array
from copy import deepcopy


def hello():
    return 'hello'

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

def position_is_already_taken(line: int, row: int, sudoku_or_quadrant: array) -> bool:
        if sudoku_or_quadrant[line][row][0] == None:
            return False
        else:
            return True

def get_coordinates_in_quadrant(quadrant_index: int) -> array:
    quadrant_coordinates: array = []

    upper_line = quadrant_index - (quadrant_index % 3)
    left_row = (quadrant_index % 3) * 3
    upper_left_coordinate = [upper_line, left_row]

    for current_line in range(0, 3):
        for current_row in range(0, 3):
            coordinate_line = upper_left_coordinate[0] + current_line
            coordinate_row = upper_left_coordinate[1] + current_row
            quadrant_coordinates.append([coordinate_line, coordinate_row])
    return quadrant_coordinates

def get_quadrant_index_of_position(line: int, row: int) -> int:
    quadrant_line = int(line / 3)
    quadrant_row = int(row / 3)
    quadrant_index = quadrant_row + (quadrant_line * 3)
    return quadrant_index

def position_is_in_quadrant(line: int, row: int, quadrant_index_of_position: int) -> bool:
    quadrant_index = get_quadrant_index_of_position(line, row)
    if quadrant_index == quadrant_index_of_position:
        return True
    else:
        return False

def position_has_blocking_number(number: int, line: int, row: int, sudoku_to_work_on: array) -> bool:
    blocking_number_list: array = sudoku_to_work_on[line][row][1]
    for blocking_number in blocking_number_list:
        if blocking_number == number:
            return True
    return False