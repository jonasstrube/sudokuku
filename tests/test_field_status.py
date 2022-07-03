import pytest

from sudokuku.field_status import FieldStatus

class TestFieldStatus:

    def test_field_status(self):
        assert FieldStatus.EMPTY == 0
        assert FieldStatus.BLOCKED == 1
        assert FieldStatus.FILLED == 2