from array import array
from copy import deepcopy
from random import randint
import __sudokumanager 

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

def print_sudoku(sudoku: array):
    for line in sudoku:
        line_str: str = ''
        for box in line:
            if box[0]:
                line_str += str(box[0]) + ' '
            else:
                line_str += '  '
        print(line_str)

def main():

    sudoku_input = get_sudoku_input()

    # UGLY editing of sudoku in highlevel function
    # TODO move to get_sudoku_input() or move to new function in sudokumanager, that gets executed by get_sudoku_input()
    for line in range(9):
        for row in range(9):
            sudoku_input[line][row] = [sudoku_input[line][row], []]

    print()
    print('Start:')
    print_sudoku(sudoku_input)
    print()

    sudoku_solved = __sudokumanager.solve_sudoku(sudoku_input)

    print('End:')
    print_sudoku(sudoku_solved)
    print()
    # print("Iterations: " + str(iterations))
    print (__sudokumanager.hello())

if __name__== '__main__':
    main()