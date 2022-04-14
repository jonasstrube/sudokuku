from array import array
from copy import deepcopy
from random import randint
import __sudokumanager 

# TODO move sudoku access methods to its own class for better overview

def __quadrantline_is_blocked_by_blocking_numbers(number: int, line_quadrantrelative: int, current_quadrant: array) -> bool:
    possible_positions = []
    for line in range(0, 3):
        for row in range(0, 3):
            if not __sudokumanager.position_is_already_taken(line, row, current_quadrant):
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

def __quadrantrow_is_blocked_by_blocking_numbers(number: int, row_quadrantrelative: int, current_quadrant: array) -> bool:
    possible_positions = []
    for line in range(0, 3):
        for row in range(0, 3):
            if not __sudokumanager.position_is_already_taken(line, row, current_quadrant):
                possible_numbers_list = current_quadrant[line][row][1]
                for possible_number in possible_numbers_list:
                    if possible_number == number:
                        possible_positions.append([line, row])
    return False

def __blocking_numbers_in_line_or_row(number: int, line: int, row: int, sudoku_to_work_on: array) -> bool:
    quadrant_index_of_position: int = __sudokumanager.get_quadrant_index_of_position(line, row)
    line_quadrantrelative = line % 3
    row_quadrantrelative = row % 3
    for current_row in range(0, 9):
        if not __sudokumanager.position_is_in_quadrant(line, current_row, quadrant_index_of_position) and sudoku_to_work_on[line][current_row][0] == None:
            if __sudokumanager.number_is_possible_on_position(number, line, current_row, sudoku_to_work_on):
                current_quadrant_index = __sudokumanager.get_quadrant_index_of_position(line, current_row)
                current_quadrant = __sudokumanager.get_quadrant(current_quadrant_index, sudoku_to_work_on)
                if __quadrantline_is_blocked_by_blocking_numbers(number, line_quadrantrelative, current_quadrant):
                    return True

    for current_line in range(0, 9):
        if not __sudokumanager.position_is_in_quadrant(current_line, row, quadrant_index_of_position) and sudoku_to_work_on[current_line][row][0] == None:
            if __sudokumanager.number_is_possible_on_position(number, current_line, row, sudoku_to_work_on):
                current_quadrant_index = __sudokumanager.get_quadrant_index_of_position(current_line, row)
                current_quadrant = __sudokumanager.get_quadrant(current_quadrant_index, sudoku_to_work_on)
                if __quadrantrow_is_blocked_by_blocking_numbers(number, row_quadrantrelative, current_quadrant):
                    return True
    
    return False

def __number_fits_in_position(number: int, line: int, row: int, sudoku_to_work_on: array) -> bool:
    if (    __sudokumanager.same_number_in_line_or_row(number, line, row, sudoku_to_work_on) 
        or __blocking_numbers_in_line_or_row(number, line, row, sudoku_to_work_on)):
        return False
    else:
        return True

def print_sudoku(sudoku: array):
    for line in sudoku:
        line_str: str = ''
        for box in line:
            if box[0]:
                line_str += str(box[0]) + ' '
            else:
                line_str += '  '
        print(line_str)

def coordinates_are_in_line(coordinates: array) -> bool:
    possible_coordinates_local = deepcopy(coordinates)

    line_candidate = possible_coordinates_local[0][0]
    row_candidate = possible_coordinates_local[0][1]
    del(possible_coordinates_local[0])
    for coordinate in possible_coordinates_local:
        if line_candidate or row_candidate:
            if not line_candidate == coordinate[0]:
                line_candidate = None
            if not row_candidate == coordinate[1]:
                row_candidate = None
    
    if line_candidate or row_candidate:
        return True
    else:
        return False 

def block_line_or_row(number: int, blocking_positions: array, sudoku: array) -> None:
    for position in blocking_positions:
        blocking_numbers = sudoku[position[0]][position[1]][1]
        for blocking_number in blocking_numbers:
            if number == blocking_number:
                return None
    for position in blocking_positions:
        sudoku[position[0]][position[1]][1].append(number)

def number_is_already_in_quadrant(number: int, quadrant_index: int, sudoku_to_work_on: array) -> bool:
    quadrant = __sudokumanager.get_quadrant(quadrant_index, sudoku_to_work_on)

    for line in quadrant:
        for field in line:
            if field[0] == number:
                return True
    return False

def get_possible_coordinates_of_number(number: int, quadrant_index: int, sudoku_to_work_on: array) -> array:
    possible_coordinates: array = []
    for line_quadrantrelative in range(0, 3):
        line = line_quadrantrelative + quadrant_index - (quadrant_index % 3)
        for row_quadrantrelative in range(0, 3):
            row = row_quadrantrelative + (quadrant_index % 3) * 3
            if __sudokumanager.position_is_already_taken(line, row, sudoku_to_work_on):
                pass
            elif __number_fits_in_position(number, line, row, sudoku_to_work_on):
                possible_coordinates.append([line, row])
            else:
                # number does not fit the position
                pass
    
    return possible_coordinates

def work_sudoku(sudoku: array) -> None:
    for number in range(1, 10): # 1 to 9
        for quadrant_index in range(9): # 9 quadrants, 0 to 8 
            if not number_is_already_in_quadrant(number, quadrant_index, sudoku):
                # fill in number if it only has one possible position 
                possible_coordinates = get_possible_coordinates_of_number(number, quadrant_index, sudoku)
                
                if len(possible_coordinates) == 1:
                    line = possible_coordinates[0][0]
                    row = possible_coordinates[0][1]
                    sudoku[line][row][0] = number
                    __sudokumanager.erase_possible_numbers_at_position(line, row, sudoku)
                    __sudokumanager.erase_possible_positions_of_number(number, quadrant_index, sudoku)
                elif len(possible_coordinates) > 1:
                    block_possible = coordinates_are_in_line(possible_coordinates)
                    if block_possible:
                        block_line_or_row(number, possible_coordinates, sudoku)
                else:
                    # Exception: there is no possible coordinate in the given quadrant for the number
                    raise Exception
            else:
                # number is already in quadrant
                pass

def get_sudoku_input() -> array:

    prepared_sudokus: dict = {
        4: [
            [
                [None, None, 6, 5, None, 7, 4, None, None],
                [None, 8, None, 9, None, 3, None, 6, None],
                [3, None, None, None, None, None, None, None, 5],
                [7, 6, None, None, 4, None, None, 8, 2],
                [None, None, None, 6, None, 8, None, None, None],
                [8, 5, None, None, 9, None, None, 1, 3],
                [5, None, None, None, None, None, None, None, 8],
                [None, 1, None, 2, None, 9, None, 7, None],
                [None, None, 7, 8, None, 4, 1, None, None]
            ]
        ],
        6: [
            [
                [3, None, None, 8, None, None, 4, 1, None],
                [None, None, None, 2, 3, None, None, None, 5],
                [None, None, 8, None, None, 1, None, None, 3],
                [6, None, 4, None, None, None, 2, None, None],
                [1, None, 9, 6, None, None, None, 5, None],
                [None, None, None, None, 8, None, None, 3, 6],
                [8, None, None, None, 2, 7, 3, None, None],
                [None, 9, None, None, None, None, None, 6, None],
                [7, None, 1, None, 6, 9, None, 4, 8]
            ]
        ]
    }

    print('manual input (m) or prepared sudoku(p)?')
    decision_mp_str = input()
    if decision_mp_str == 'm':
        new_sudoku: array = [] 
        line_count = range(0, 9)
        for line in line_count:
            input_str = input()
            new_line: array = []
            for character in input_str:
                try:
                    input_int = int(character)
                except:
                    if character == ' ' or '0':
                        input_int = None
                    else:
                        print('wrong symbol, try again (only 1-9 and space or 0)')
                        line_count.step(1)
                        break
                new_line.append(input_int)
            if len(new_line) == 9:
                new_sudoku.append(new_line)
        return new_sudoku
    elif decision_mp_str == 'p':
        print('difficulty [4/6] and random (r) or specific(0-1)')
        decision_dri_str = input()
        difficulty: int = int(decision_dri_str[0])
        decision_random_str = decision_dri_str[1]
        if decision_random_str == 'r':
            sudokus_from_chosen_difficulty = prepared_sudokus[difficulty]
            index: int = randint(0, len(sudokus_from_chosen_difficulty) - 1)
            return sudokus_from_chosen_difficulty[index]
        else:
            id: int = int(decision_dri_str[1])
            return prepared_sudokus[difficulty][id]
    else:
        print('that didnt work')
        return None

def main():

    sudoku_input = get_sudoku_input()

    for line in range(9):
        for row in range(9):
            sudoku_input[line][row] = [sudoku_input[line][row], []]

    print()
    print('Start:')
    print_sudoku(sudoku_input)

    sudoku_to_work_on = deepcopy(sudoku_input)
    sudoku_last_state = None
    iterations = 0
    while(not sudoku_last_state == sudoku_to_work_on): # while something is changing
        iterations += 1
        sudoku_last_state = deepcopy(sudoku_to_work_on)

        work_sudoku(sudoku_to_work_on)

    print('End:')    
    print_sudoku(sudoku_to_work_on)
    print()
    print("Iterations: " + str(iterations))
    print (__sudokumanager.hello())

if __name__== '__main__':
    main()