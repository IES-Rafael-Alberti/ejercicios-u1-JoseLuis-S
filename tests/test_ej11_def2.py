import pytest
from src.ej11_def2 import sumNum

@pytest.mark.parametrize(
    'num, expected',
    [
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
    ]
)
def test_sumNum(num, expected):
    assert sumNum(num) == expected