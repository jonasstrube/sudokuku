class CoordinateCalculator:
    @staticmethod
    def calculate_sudoku_index_from_quadrantrelative_index(quadrant_index: int, line_index_quadrantrelative: int, column_index_quadrantrelative: int):
        line_index = None
        column_index = None
        if not line_index_quadrantrelative == None:
            line_index = line_index_quadrantrelative + quadrant_index - (quadrant_index % 3)
        if not column_index_quadrantrelative == None:
            column_index = column_index_quadrantrelative + (quadrant_index % 3) * 3
        
        if column_index and line_index: return [line_index, column_index]
        elif line_index:                return line_index
        else:                           return column_index
