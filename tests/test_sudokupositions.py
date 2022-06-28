import pytest
from src.sudokuku import manager

class TestSudokuPositions():
    
    def test_coordinates_are_in_line(self):
        coordinates = [[3, 3], [3, 4], [5, 3]]
        assert manager.coordinates_are_in_line(coordinates) == False
        
        coordinates = [[3, 8], [5, 6]]
        assert manager.coordinates_are_in_line(coordinates) == False

        coordinates = [[7, 7], [7, 8]]
        assert manager.coordinates_are_in_line(coordinates) == True

        coordinates = [[7, 6], [7, 7], [7, 8]]
        assert manager.coordinates_are_in_line(coordinates) == True
        
        coordinates = None
        with pytest.raises(TypeError):
            manager.coordinates_are_in_line(coordinates)

        coordinates = [[8, 4]]
        with pytest.raises(ValueError):
            manager.coordinates_are_in_line(coordinates)
