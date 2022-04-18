from array import array
from copy import deepcopy


def hello():
    return 'hello'

# -----------------------------------------------
# SUDOKU POSITIONS - ACCESS
# -----------------------------------------------

def position_is_already_taken(line: int, row: int, sudoku_or_quadrant: array) -> bool:
        if sudoku_or_quadrant[line][row][0] == None:
            return False
        else:
            return True

def same_number_in_line_or_row(number: int, line: int, row: int, sudoku_to_work_on: array) -> bool:
    for current_row in range(0, 9):
        # UGLY dezentralized sudoku access
        if sudoku_to_work_on[line][current_row][0] == number:
            return True
    
    for current_line in range(0, 9):
        # UGLY dezentralized sudoku access
        if sudoku_to_work_on[current_line][row][0] == number:
            return True
    
    return False

# -----------------------------------------------
# SUDOKU POSSIBLE POSITIONS OF NUMBERS - ACCESS AND MANIPULATION
# -----------------------------------------------

def blocking_numbers_in_line_or_row(number: int, line: int, row: int, sudoku_to_work_on: array) -> bool:
    quadrant_index_of_position: int = get_quadrant_index_of_position(line, row)
    line_quadrantrelative = line % 3
    row_quadrantrelative = row % 3
    for current_row in range(0, 9):
        if not position_is_in_quadrant(line, current_row, quadrant_index_of_position) and sudoku_to_work_on[line][current_row][0] == None:
            if number_is_possible_on_position(number, line, current_row, sudoku_to_work_on):
                current_quadrant_index = get_quadrant_index_of_position(line, current_row)
                current_quadrant = get_quadrant(current_quadrant_index, sudoku_to_work_on)
                if quadrantline_is_blocked_by_blocking_numbers(number, line_quadrantrelative, current_quadrant):
                    return True

    for current_line in range(0, 9):
        if not position_is_in_quadrant(current_line, row, quadrant_index_of_position) and sudoku_to_work_on[current_line][row][0] == None:
            if number_is_possible_on_position(number, current_line, row, sudoku_to_work_on):
                current_quadrant_index = get_quadrant_index_of_position(current_line, row)
                current_quadrant = get_quadrant(current_quadrant_index, sudoku_to_work_on)
                if quadrantrow_is_blocked_by_blocking_numbers(number, row_quadrantrelative, current_quadrant):
                    return True
    
    return False

def number_is_possible_on_position(number: int, line: int, row: int, sudoku_to_work_on: array) -> bool:
    blocking_number_list: array = sudoku_to_work_on[line][row][1]
    for blocking_number in blocking_number_list:
        if blocking_number == number:
            return True
    return False

def erase_possible_positions_of_number(number: int, quadrant_index: int, sudoku: array) -> None:
    quadrant_position_list = get_coordinates_in_quadrant(quadrant_index)
    
    for quadrant_position in quadrant_position_list:
        possible_positions = sudoku[quadrant_position[0]][quadrant_position[1]][1]
        for index in range(len(possible_positions)):
            if possible_positions[index] == number:
                del(possible_positions[index])
                break

def erase_possible_numbers_at_position(line: int, row: int, sudoku: array) -> None:
    sudoku[line][row][1] = []

# -----------------------------------------------
# QUADRANTS POSITIONS - ACCESS AND HELPER FUNCTIONS
# -----------------------------------------------

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

def number_is_in_quadrant(number: int, quadrant_index: int, sudoku_to_work_on: array) -> bool:
    quadrant = get_quadrant(quadrant_index, sudoku_to_work_on)

    for line in quadrant:
        for field in line:
            if field[0] == number:
                return True
    return False

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

# -----------------------------------------------
# QUADRANTS POSSIBLE POSITIONS OF NUMBERS - ACCESS
# -----------------------------------------------

def quadrantline_is_blocked_by_blocking_numbers(number: int, line_quadrantrelative: int, current_quadrant: array) -> bool:
    possible_positions = []
    for line in range(0, 3):
        for row in range(0, 3):
            if not position_is_already_taken(line, row, current_quadrant):
                possible_numbers_list = current_quadrant[line][row][1]
                for possible_number in possible_numbers_list:
                    if possible_number == number:
                        possible_positions.append([line, row])

    if len(possible_positions) == 0:
        return False
    for position in possible_positions:
        if not line_quadrantrelative == position[0]:
            return False
    return True

def quadrantrow_is_blocked_by_blocking_numbers(number: int, row_quadrantrelative: int, current_quadrant: array) -> bool:
    possible_positions = []
    for line in range(0, 3):
        for row in range(0, 3):
            if not position_is_already_taken(line, row, current_quadrant):
                possible_numbers_list = current_quadrant[line][row][1]
                for possible_number in possible_numbers_list:
                    if possible_number == number:
                        possible_positions.append([line, row])

    # TODO implement True condition (see function above)
    return False

