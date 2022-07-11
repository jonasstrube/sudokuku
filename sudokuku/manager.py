from array import array
from copy import deepcopy
from dataclasses import Field

from sudokuku.field_state import FieldState
from sudokuku.sudokuwrapped import Sudokuwrapped
from sudokuku.coordinate_calculator import CoordinateCalculator
from sudokuku.sudoku_handler import SudokuHandler

# TODO change use of data type array to list (e.g. sudoku and quadrant)
# TODO rename position to field or coordinate, depending on content.
# pure coordinate = ccordinate
# list containing ccordinate, number and FieldState = field

def solve_sudoku(sudoku: array) -> Sudokuwrapped:
    sudoku_input = deepcopy(sudoku)
    sudoku_iterated: array = SudokuHandler.prepare_sudoku(sudoku_input)
    sudoku_old_state: array = None
    iterations = 0
    while(not sudoku_iterated == sudoku_old_state): # as long as something is changing
        sudoku_old_state = sudoku_iterated
        sudoku_iterated: array = iterate_sudoku(sudoku_old_state)
        iterations += 1
    
    sudoku_cleaned = SudokuHandler.clean_sudoku(sudoku_old_state)
    sudoku_wrapped = Sudokuwrapped(sudoku_cleaned, iterations)
    return sudoku_wrapped

def iterate_sudoku(sudoku: array) -> array:
    sudoku: array = deepcopy(sudoku)
    for number in range(1, 10): # 1 to 9
        for quadrant_index in range(9): # 9 quadrants, 0 to 8 
            if not number_is_in_quadrant(number, quadrant_index, sudoku):
                possible_coordinates = determine_possible_coordinates_of_number(number, sudoku, quadrant_index=quadrant_index)
                
                if len(possible_coordinates) == 1:
                    # fill in number if it only has one possible position
                    line_to_write = possible_coordinates[0][0]
                    column_to_write = possible_coordinates[0][1]
                    SudokuHandler.set_number(number, line_to_write, column_to_write, sudoku)
                    SudokuHandler.delete_possible_numbers(line_index=line_to_write, column_index=column_to_write, sudoku=sudoku)
                    erase_possible_positions_of_number(number, quadrant_index, sudoku)
                elif len(possible_coordinates) > 1:
                    block_possible = coordinates_are_in_line(possible_coordinates)
                    if block_possible:
                        set_possible_positions_of_number(number, possible_coordinates, sudoku)
                    fields_and_numbers_to_block = determine_fields_and_numbers_blocked_by_possible_numbers(number, quadrant_index, sudoku)
                    if len(fields_and_numbers_to_block) > 0:
                        numbers_to_block = fields_and_numbers_to_block[0]
                        fields_to_block = fields_and_numbers_to_block[1]
                        for field in fields_to_block:
                            numbers_not_anymore_possible_at_field = list(set(field[1]) - set(numbers_to_block))
                            SudokuHandler.delete_possible_numbers(line_index=field[0][0], column_index=field[0][1], sudoku=sudoku, numbers_to_remove=numbers_not_anymore_possible_at_field)
                            SudokuHandler.set_field_state(field[0][0], field[0][1], FieldState.BLOCKED, sudoku)
                else:
                    # Exception: there is no possible coordinate in the given quadrant for the number
                    raise Exception
            else:
                # number is already in quadrant
                pass
                
        for line_index in range(9): # 0 to 8
            if not same_number_in_line_or_column(number, sudoku, line_index=line_index):
                # TODO implement search for coordinates in line in get_possible_coordinates_of_number
                possible_coordinates = determine_possible_coordinates_of_number(number, sudoku, line_index=line_index)

                if len(possible_coordinates) == 1:
                    line_to_write = possible_coordinates[0][0]
                    column_to_write = possible_coordinates[0][1]
                    SudokuHandler.set_number(number, line_to_write, column_to_write, sudoku)
                    SudokuHandler.delete_possible_numbers(line_index=line_to_write, column_index=column_to_write, sudoku=sudoku)
                    quadrant_index = get_quadrant_index_of_position(line_to_write, column_to_write)
                    erase_possible_positions_of_number(number, quadrant_index, sudoku)
                elif len(possible_coordinates) == 0:
                    # Exception: there is no possible coordinate in the given line for the number
                    raise Exception
            else:
                # number is already in line
                pass
        
        for column_index in range(9): # 0 to 8
            if not same_number_in_line_or_column(number, sudoku, column_index=column_index):
                # TODO implement search for coordinates in column in get_possible_coordinates_of_number
                possible_coordinates = determine_possible_coordinates_of_number(number, sudoku, column_index=column_index)

                if len(possible_coordinates) == 1:
                    line_to_write = possible_coordinates[0][0]
                    column_to_write = possible_coordinates[0][1]
                    SudokuHandler.set_number(number, line_to_write, column_to_write, sudoku)
                    SudokuHandler.delete_possible_numbers(line_index=line_to_write, column_index=column_to_write, sudoku=sudoku)
                    quadrant_index = get_quadrant_index_of_position(line_to_write, column_to_write)
                    erase_possible_positions_of_number(number, quadrant_index, sudoku)
                elif len(possible_coordinates) == 0:
                    # Exception: there is no possible coordinate in the given line for the number
                    raise Exception
            else:
                # number is already in line
                pass

    return sudoku

# -----------------------------------------------
# SUDOKU POSITIONS - ACCESS, MANIPULATION AND HELPER FUNCTIONS
# -----------------------------------------------

def field_is_not_possible_for_number(number: int, line_index: int, column_index: int, sudoku_or_quadrant: array) -> bool:
        if (sudoku_or_quadrant[line_index][column_index][0] == None 
        and not field_is_blocked_for_number(number, line_index, column_index, sudoku_or_quadrant)):
            return False
        else:
            return True

def same_number_in_line_or_column(number: int, sudoku_to_work_on: array, line_index=None, column_index=None) -> bool:
    if not line_index == None:
        for current_column_index in range(0, 9):
            sudoku_number: int = SudokuHandler.get_number(line_index, current_column_index, sudoku_to_work_on)
            if sudoku_number == number:
                return True
    
    if not column_index == None:
        for current_line_index in range(0, 9):
            sudoku_number: int = SudokuHandler.get_number(current_line_index, column_index, sudoku_to_work_on)
            if sudoku_number == number:
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
        for number in line:
            if number:
                line_str += str(number) + ' '
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
            if number_is_in_possible_numbers_in_field(number, line, current_column, sudoku_to_work_on):
                current_quadrant_index = get_quadrant_index_of_position(line, current_column)
                current_quadrant = SudokuHandler.get_quadrant(current_quadrant_index, sudoku_to_work_on)
                if quadrantline_is_blocked_by_blocking_numbers(number, line_quadrantrelative, current_quadrant):
                    return True

    for current_line in range(0, 9):
        if not position_is_in_quadrant(current_line, column, quadrant_index_of_position) and sudoku_to_work_on[current_line][column][0] == None:
            if number_is_in_possible_numbers_in_field(number, current_line, column, sudoku_to_work_on):
                current_quadrant_index = get_quadrant_index_of_position(current_line, column)
                current_quadrant = SudokuHandler.get_quadrant(current_quadrant_index, sudoku_to_work_on)
                if quadrantcolumn_is_blocked_by_blocking_numbers(number, column_quadrantrelative, current_quadrant):
                    return True
    
    return False

def number_is_in_possible_numbers_in_field(number: int, line: int, column: int, sudoku_to_work_on: array) -> bool:
    blocking_number_list: array = sudoku_to_work_on[line][column][1]
    for blocking_number in blocking_number_list:
        if blocking_number == number:
            return True
    return False

def determine_if_number_fits_in_field(number: int, line: int, column: int, sudoku_to_work_on: array) -> bool:
    quadrant_index = get_quadrant_index_of_position(line, column)

    if (same_number_in_line_or_column(number, sudoku_to_work_on, line, column)
    or number_is_in_quadrant(number, quadrant_index, sudoku_to_work_on) 
    or blocking_numbers_in_line_or_column(number, line, column, sudoku_to_work_on)):
        return False
    else:
        return True

def erase_possible_positions_of_number(number: int, quadrant_index: int, sudoku: array) -> None:
    quadrant_coordinates_list = get_coordinates_in_quadrant(quadrant_index)
    
    for quadrant_coordinate in quadrant_coordinates_list:
        SudokuHandler.delete_possible_numbers(quadrant_coordinate[0], quadrant_coordinate[1], sudoku, number)

def set_possible_positions_of_number(number: int, possible_position_coordinates: array, sudoku_to_work_on: array) -> None:
    for position in possible_position_coordinates:
        possible_numbers = SudokuHandler.get_possible_numbers(position[0], position[1], sudoku_to_work_on)
        for possible_number in possible_numbers:
            if number == possible_number:
                return None
    for position in possible_position_coordinates:
        SudokuHandler.add_possible_number(number, position[0], position[1], sudoku_to_work_on)

# -----------------------------------------------
# QUADRANTS POSITIONS - ACCESS AND HELPER FUNCTIONS
# -----------------------------------------------

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
    quadrant = SudokuHandler.get_quadrant(quadrant_index, sudoku_to_work_on)

    for line in quadrant:
        for field in line:
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
# QUADRANTS POSSIBLE POSITIONS OF NUMBERS - ACCESS AND MANIPULATION
# -----------------------------------------------

def quadrantline_is_blocked_by_blocking_numbers(number: int, line_quadrantrelative: int, current_quadrant: array) -> bool:
    possible_positions = []
    for line in range(0, 3):
        for column in range(0, 3):
            if not field_is_not_possible_for_number(number, line, column, current_quadrant):
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
            if not field_is_not_possible_for_number(number, line, column, current_quadrant):
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

def determine_possible_coordinates_of_number(number: int, sudoku_to_work_on: array, quadrant_index=None, line_index=None, column_index=None) -> list:
    optional_argument_sum = 0
    if not quadrant_index == None: optional_argument_sum += 1
    if not line_index == None: optional_argument_sum += 1
    if not column_index == None: optional_argument_sum += 1

    if not optional_argument_sum == 1:
        # exception: only one argument allowed: quadrant_index, line_index or column_index
        # this function can only scan for possible coordinates in ONE of quadrants or lines or columns
        raise Exception

    possible_coordinates = []
    if not quadrant_index == None:
        for line_quadrantrelative in range(0, 3):
            line_index = line_quadrantrelative + quadrant_index - (quadrant_index % 3)
            for column_quadrantrelative in range(0, 3):
                column_index = column_quadrantrelative + (quadrant_index % 3) * 3
                if field_is_not_possible_for_number(number, line_index, column_index, sudoku_to_work_on):
                    pass
                elif determine_if_number_fits_in_field(number, line_index, column_index, sudoku_to_work_on):
                    possible_coordinates.append([line_index, column_index])
                else:
                    # number does not fit the position
                    pass
    elif not line_index == None:
        for column_index in range(9):
            if field_is_not_possible_for_number(number, line_index, column_index, sudoku_to_work_on):
                pass
            elif determine_if_number_fits_in_field(number, line_index, column_index, sudoku_to_work_on):
                possible_coordinates.append([line_index, column_index])
            else:
                # number does not fit the position
                pass
    elif not column_index == None:
        for line_index in range(9):
            if field_is_not_possible_for_number(number, line_index, column_index, sudoku_to_work_on):
                pass
            elif determine_if_number_fits_in_field(number, line_index, column_index, sudoku_to_work_on):
                possible_coordinates.append([line_index, column_index])
            else:
                # number does not fit the position
                pass
    
    return possible_coordinates

def get_coordinates_with_possible_number_in_quadrant(number: int, quadrant_index: int, sudoku_to_work_on: list) -> list:
    quadrant = SudokuHandler.get_quadrant(quadrant_index, sudoku_to_work_on)
    
    coordinates_with_possible_number = []
    for line_index in range(len(quadrant)):
        line = quadrant[line_index]
        for column_index in range(len(line)):
            field = line[column_index]
            field_value: int = field[0]
            field_possible_numbers: list = field[1]
            field_state: FieldState = field[2]
            if (    (field_value == None)    
                and (field_state == FieldState.EMPTY or field_state == FieldState.BLOCKED) 
                and (number in field_possible_numbers)):
                coordinate = CoordinateCalculator.calculate_sudoku_index_from_quadrantrelative_index(quadrant_index, line_index, column_index)
                coordinates_with_possible_number.append(coordinate)

    return coordinates_with_possible_number

def determine_fields_and_numbers_blocked_by_possible_numbers(number: int, quadrant_index: int, sudoku_to_work_on: list) -> list:
    ## if in every blocked coordinate are as many possible numbers, as possible coordinates for the current number, BUT all of these numbers dont fit anywhere else in the quadrant:
    ##   give out all of these coordinates
    
    possible_coordinates: list = deepcopy(get_coordinates_with_possible_number_in_quadrant(number, quadrant_index, sudoku_to_work_on))

    possible_fields = []
    for coordinate in possible_coordinates:
        possible_numbers = SudokuHandler.get_possible_numbers(coordinate[0], coordinate[1], sudoku_to_work_on)
        possible_fields.append([coordinate, possible_numbers])
    
    count_of_possible_fields = len(possible_fields)

    all_distinct_possible_numbers = set()
    for field in possible_fields:
        possible_numbers = field[1]
        for current_number in possible_numbers:
            possible_coordinates_of_current_number: list = deepcopy(get_coordinates_with_possible_number_in_quadrant(current_number, quadrant_index, sudoku_to_work_on))
            if sorted(possible_coordinates_of_current_number) == sorted(possible_coordinates):
                all_distinct_possible_numbers.add(current_number)

    if not len(all_distinct_possible_numbers) == count_of_possible_fields:
        if len(all_distinct_possible_numbers) > count_of_possible_fields:
            return []
        else:
            # TODO when the package marks every possible number in quadrants in the future: raise Exception, as it cant happen that e.g. only 2 numbers fit 3 fields
            return [] 

    fields_to_block_by_numbers = [list(all_distinct_possible_numbers), possible_fields]
    return deepcopy(fields_to_block_by_numbers)

def field_is_blocked_for_number(number: int, line_index: int, column_index: int, sudoku_to_work_on: list) -> bool:
    possible_numbers = SudokuHandler.get_possible_numbers(line_index, column_index, sudoku_to_work_on)
    field_state = SudokuHandler.get_field_state(line_index, column_index, sudoku_to_work_on)
    return (field_state == FieldState.BLOCKED) and (not number in possible_numbers)
