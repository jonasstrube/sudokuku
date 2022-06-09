from array import array
from copy import deepcopy

from sudokuku.sudokuwrapped import Sudokuwrapped

# TODO change data type of sudoku and quadrant from array to list
# TODO change all other uses of array datatype to list datatype

def solve_sudoku(sudoku: array) -> Sudokuwrapped:
    sudoku_input = deepcopy(sudoku)
    sudoku_iterated: array = deepcopy(sudoku_input)
    sudoku_old_state: array = None
    iterations = 0
    while(not sudoku_iterated == sudoku_old_state): # while something is changing
        sudoku_old_state = sudoku_iterated
        sudoku_iterated: array = iterate_sudoku(sudoku_old_state)
        iterations += 1
    
    sudoku_wrapped = Sudokuwrapped(sudoku_old_state, iterations)
    return sudoku_wrapped

def iterate_sudoku(sudoku: array) -> array:
    sudoku: array = deepcopy(sudoku)
    for number in range(1, 10): # 1 to 9
        for quadrant_index in range(9): # 9 quadrants, 0 to 8 
            if not number_is_in_quadrant(number, quadrant_index, sudoku):
                possible_coordinates = get_possible_coordinates_of_number(number, sudoku, quadrant=quadrant_index)
                
                if len(possible_coordinates) == 1:
                    # fill in number if it only has one possible position 
                    # UGLY decentralized access of sudoku
                    line = possible_coordinates[0][0]
                    column = possible_coordinates[0][1]
                    sudoku[line][column][0] = number
                    erase_possible_numbers_at_position(line, column, sudoku)
                    erase_possible_positions_of_number(number, quadrant_index, sudoku)
                elif len(possible_coordinates) > 1:
                    block_possible = coordinates_are_in_line(possible_coordinates)
                    if block_possible:
                        block_line_or_column(number, possible_coordinates, sudoku)
                else:
                    # Exception: there is no possible coordinate in the given quadrant for the number
                    raise Exception
            else:
                # number is already in quadrant
                pass
                
        for line_index in range(9): # 0 to 8
            if not same_number_in_line_or_column(number, sudoku, line=line_index):
                # TODO implement search for coordinates in line in get_possible_coordinates_of_number
                possible_coordinates = get_possible_coordinates_of_number(number, sudoku, line=line_index)

                if len(possible_coordinates) == 1:
                    # UGLY decentralized access of sudoku
                    line = possible_coordinates[0][0]
                    column = possible_coordinates[0][1]
                    sudoku[line][column][0] = number
                    erase_possible_numbers_at_position(line, column, sudoku)
                    quadrant_index = get_quadrant_index_of_position(line, column)
                    erase_possible_positions_of_number(number, quadrant_index, sudoku)
                elif len(possible_coordinates) == 0:
                    # Exception: there is no possible coordinate in the given line for the number
                    raise Exception
            else:
                # number is already in line
                pass
        
        for column_index in range(9): # 0 to 8
            if not same_number_in_line_or_column(number, sudoku, column=column_index):
                # TODO implement search for coordinates in column in get_possible_coordinates_of_number
                possible_coordinates = get_possible_coordinates_of_number(number, sudoku, column=column_index)

                if len(possible_coordinates) == 1:
                    # UGLY decentralized access of sudoku
                    line = possible_coordinates[0][0]
                    column = possible_coordinates[0][1]
                    sudoku[line][column][0] = number
                    erase_possible_numbers_at_position(line, column, sudoku)
                    quadrant_index = get_quadrant_index_of_position(line, column)
                    erase_possible_positions_of_number(number, quadrant_index, sudoku)
                elif len(possible_coordinates) == 0:
                    # Exception: there is no possible coordinate in the given line for the number
                    raise Exception
            else:
                # number is already in line
                pass

    return sudoku

def prepare_sudoku(sudoku_raw: array) -> array:
    sudoku = deepcopy(sudoku_raw)
    for line in range(9):
        for column in range(9):
            sudoku[line][column] = [sudoku[line][column], []]
    return sudoku

# -----------------------------------------------
# SUDOKU POSITIONS - ACCESS AND HELPER FUNCTIONS
# -----------------------------------------------

def position_is_already_taken(line: int, column: int, sudoku_or_quadrant: array) -> bool:
        if sudoku_or_quadrant[line][column][0] == None:
            return False
        else:
            return True

def same_number_in_line_or_column(number: int, sudoku_to_work_on: array, line=None, column=None) -> bool:
    if not line == None:
        for current_column in range(0, 9):
            # UGLY dezentralized sudoku access
            if sudoku_to_work_on[line][current_column][0] == number:
                return True
    
    if not column == None:
        for current_line in range(0, 9):
            # UGLY dezentralized sudoku access
            if sudoku_to_work_on[current_line][column][0] == number:
                return True
    
    return False

def coordinates_are_in_line(coordinates: list) -> bool:
    if not isinstance(coordinates, list):
        raise TypeError('\'' + str(type(coordinates)) + '\' object is not allowed as an argument, coordinates have to be of type \'list\'')
    if len(coordinates) < 2:
        raise ValueError('length of coordinates list is ' + str(len(coordinates)) + ', must be at least 2')

    possible_coordinates_local = deepcopy(coordinates)

    line_candidate = possible_coordinates_local[0][0]
    column_candidate = possible_coordinates_local[0][1]
    del(possible_coordinates_local[0])
    for coordinate in possible_coordinates_local:
        if line_candidate or column_candidate:
            if not line_candidate == coordinate[0]:
                line_candidate = None
            if not column_candidate == coordinate[1]:
                column_candidate = None
    
    if line_candidate or column_candidate:
        return True
    else:
        return False 

def print_sudoku(sudoku: array):
    for line in sudoku:
        line_str: str = ''
        for box in line:
            if box[0]:
                line_str += str(box[0]) + ' '
            else:
                line_str += '  '
        print(line_str)

# -----------------------------------------------
# SUDOKU POSSIBLE POSITIONS OF NUMBERS - ACCESS AND MANIPULATION
# -----------------------------------------------

def blocking_numbers_in_line_or_column(number: int, line: int, column: int, sudoku_to_work_on: array) -> bool:
    quadrant_index_of_position: int = get_quadrant_index_of_position(line, column)
    line_quadrantrelative = line % 3
    column_quadrantrelative = column % 3
    for current_column in range(0, 9):
        if not position_is_in_quadrant(line, current_column, quadrant_index_of_position) and sudoku_to_work_on[line][current_column][0] == None:
            if number_is_possible_on_position(number, line, current_column, sudoku_to_work_on):
                current_quadrant_index = get_quadrant_index_of_position(line, current_column)
                current_quadrant = get_quadrant(current_quadrant_index, sudoku_to_work_on)
                if quadrantline_is_blocked_by_blocking_numbers(number, line_quadrantrelative, current_quadrant):
                    return True

    for current_line in range(0, 9):
        if not position_is_in_quadrant(current_line, column, quadrant_index_of_position) and sudoku_to_work_on[current_line][column][0] == None:
            if number_is_possible_on_position(number, current_line, column, sudoku_to_work_on):
                current_quadrant_index = get_quadrant_index_of_position(current_line, column)
                current_quadrant = get_quadrant(current_quadrant_index, sudoku_to_work_on)
                if quadrantcolumn_is_blocked_by_blocking_numbers(number, column_quadrantrelative, current_quadrant):
                    return True
    
    return False

def number_is_possible_on_position(number: int, line: int, column: int, sudoku_to_work_on: array) -> bool:
    blocking_number_list: array = sudoku_to_work_on[line][column][1]
    for blocking_number in blocking_number_list:
        if blocking_number == number:
            return True
    return False

def number_fits_in_position(number: int, line: int, column: int, sudoku_to_work_on: array) -> bool:
    if (    same_number_in_line_or_column(number, sudoku_to_work_on, line, column) 
        or blocking_numbers_in_line_or_column(number, line, column, sudoku_to_work_on)):
        return False
    else:
        return True

def erase_possible_positions_of_number(number: int, quadrant_index: int, sudoku: array) -> None:
    quadrant_position_list = get_coordinates_in_quadrant(quadrant_index)
    
    for quadrant_position in quadrant_position_list:
        possible_positions = sudoku[quadrant_position[0]][quadrant_position[1]][1]
        for index in range(len(possible_positions)):
            if possible_positions[index] == number:
                del(possible_positions[index])
                break

def erase_possible_numbers_at_position(line: int, column: int, sudoku: array) -> None:
    sudoku[line][column][1] = []

def block_line_or_column(number: int, blocking_positions: array, sudoku: array) -> None:
    for position in blocking_positions:
        # UGLY decentralized access of blocking numbers
        blocking_numbers = sudoku[position[0]][position[1]][1]
        for blocking_number in blocking_numbers:
            if number == blocking_number:
                return None
    for position in blocking_positions:
        # UGLY decentralized access of blocking numbers
        sudoku[position[0]][position[1]][1].append(number)

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
        for column in range(0, 3):
            sudoku_line = upper_left_field[0] + line
            sudoku_column = upper_left_field[1] + column
            quadrant[line][column] = deepcopy(sudoku_to_work_on[sudoku_line][sudoku_column])
    
    return quadrant

def get_quadrant_index_of_position(line: int, column: int) -> int:
    quadrant_line = int(line / 3)
    quadrant_column = int(column / 3)
    quadrant_index = quadrant_column + (quadrant_line * 3)
    return quadrant_index

def position_is_in_quadrant(line: int, column: int, quadrant_index_of_position: int) -> bool:
    quadrant_index = get_quadrant_index_of_position(line, column)
    if quadrant_index == quadrant_index_of_position:
        return True
    else:
        return False

def number_is_in_quadrant(number: int, quadrant_index: int, sudoku_to_work_on: array) -> bool:
    quadrant = get_quadrant(quadrant_index, sudoku_to_work_on)

    for line in quadrant:
        for field in line:
            # UGLY decentralized access of sudoku
            if field[0] == number:
                return True
    return False

def get_coordinates_in_quadrant(quadrant_index: int) -> array:
    quadrant_coordinates: array = []

    upper_line = quadrant_index - (quadrant_index % 3)
    left_column = (quadrant_index % 3) * 3
    upper_left_coordinate = [upper_line, left_column]

    for current_line in range(0, 3):
        for current_column in range(0, 3):
            coordinate_line = upper_left_coordinate[0] + current_line
            coordinate_column = upper_left_coordinate[1] + current_column
            quadrant_coordinates.append([coordinate_line, coordinate_column])
    return quadrant_coordinates

# -----------------------------------------------
# QUADRANTS POSSIBLE POSITIONS OF NUMBERS - ACCESS
# -----------------------------------------------

def quadrantline_is_blocked_by_blocking_numbers(number: int, line_quadrantrelative: int, current_quadrant: array) -> bool:
    possible_positions = []
    for line in range(0, 3):
        for column in range(0, 3):
            if not position_is_already_taken(line, column, current_quadrant):
                possible_numbers_list = current_quadrant[line][column][1]
                for possible_number in possible_numbers_list:
                    if possible_number == number:
                        possible_positions.append([line, column])

    if len(possible_positions) == 0:
        return False
    for position in possible_positions:
        if not line_quadrantrelative == position[0]:
            return False
    return True

def quadrantcolumn_is_blocked_by_blocking_numbers(number: int, column_quadrantrelative: int, current_quadrant: array) -> bool:
    possible_positions = []
    for line in range(0, 3):
        for column in range(0, 3):
            if not position_is_already_taken(line, column, current_quadrant):
                possible_numbers_list = current_quadrant[line][column][1]
                for possible_number in possible_numbers_list:
                    if possible_number == number:
                        possible_positions.append([line, column])

    if len(possible_positions) == 0:
        return False
    pass
    for position in possible_positions:
        if not column_quadrantrelative == position[1]:
            return False
    return True

def get_possible_coordinates_of_number(number: int, sudoku_to_work_on: array, quadrant=None, line=None, column=None) -> array:
    optional_argument_sum = 0
    if not quadrant == None: optional_argument_sum += 1
    if not line == None: optional_argument_sum += 1
    if not column == None: optional_argument_sum += 1

    if not optional_argument_sum == 1:
        # exception: only one argument allowed: quadrant_index, line_index or column_index
        # this function can only scan for possible coordinates in quadrants, lines or columns
        raise Exception

    if not quadrant == None:
        possible_coordinates: array = []
        for line_quadrantrelative in range(0, 3):
            line = line_quadrantrelative + quadrant - (quadrant % 3)
            for column_quadrantrelative in range(0, 3):
                column = column_quadrantrelative + (quadrant % 3) * 3
                if position_is_already_taken(line, column, sudoku_to_work_on):
                    pass
                elif number_fits_in_position(number, line, column, sudoku_to_work_on):
                    possible_coordinates.append([line, column])
                else:
                    # number does not fit the position
                    pass
    elif not line == None:
        possible_coordinates: array = []
        for column_index in range(9):
            if position_is_already_taken(line, column_index, sudoku_to_work_on):
                pass
            elif number_fits_in_position(number, line, column_index, sudoku_to_work_on):
                possible_coordinates.append([line, column_index])
            else:
                # number does not fit the position
                pass
    elif not column == None:
        possible_coordinates: array = []
        for line_index in range(9):
            if position_is_already_taken(line_index, column, sudoku_to_work_on):
                pass
            elif number_fits_in_position(number, line_index, column, sudoku_to_work_on):
                possible_coordinates.append([line_index, column])
            else:
                # number does not fit the position
                pass
    
    return possible_coordinates
