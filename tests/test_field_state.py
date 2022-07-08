import pytest

from sudokuku.field_state import FieldState

class TestFieldState:

    def test_field_state(self):
        assert FieldState.EMPTY == 0
        assert FieldState.BLOCKED == 1
        assert FieldState.FILLED == 2