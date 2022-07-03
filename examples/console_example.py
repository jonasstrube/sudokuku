from array import array
from random import randint

from sudokuku import manager
from sudokuku.sudokuwrapped import Sudokuwrapped 

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
        5: [
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
                [None, 9, None, None, None, None, None, None, None],
                [7, None, 1, None, 6, 9, None, None, 8]
            ]
        ]
    }

    print('manual input (m) or prepared sudoku(p)?')
    decision_mp_str = input()

    chosen_sudoku: array = None

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
        chosen_sudoku = new_sudoku
    elif decision_mp_str == 'p':
        print('difficulty [4/6] and random (r) or specific(0-1)')
        decision_dri_str = input()
        difficulty: int = int(decision_dri_str[0])
        decision_random_str = decision_dri_str[1]
        if decision_random_str == 'r':
            sudokus_from_chosen_difficulty = prepared_sudokus[difficulty]
            index: int = randint(0, len(sudokus_from_chosen_difficulty) - 1)
            chosen_sudoku = sudokus_from_chosen_difficulty[index]
        else:
            id: int = int(decision_dri_str[1])
            chosen_sudoku = prepared_sudokus[difficulty][id]
    else:
        print('that didnt work')
        return None
            
    return chosen_sudoku

def main():

    sudoku_input = get_sudoku_input()

    print()
    print('Start:')
    manager.print_sudoku(sudoku_input)
    print()

    sudoku_solved: Sudokuwrapped = manager.solve_sudoku(sudoku_input)

    print('End:')
    manager.print_sudoku(sudoku_solved.sudoku)
    print()
    print("Iterations: " + str(sudoku_solved.iterations))

if __name__== '__main__':
    main()