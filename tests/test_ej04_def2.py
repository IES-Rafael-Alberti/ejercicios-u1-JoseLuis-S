import pytest
from src.ej04_def2 import grados_celsius

@pytest.mark.parametrize(
    "grados_farenheit, expected",
    [
        (100.12, 37.84),
        (21.09, -6.06),
        (329.12, 165.07),
        (-21, -29.44),
        (200, 93.33),
    ]
)
def test_grados_farenheit_params(grados_farenheit, expected):
    assert grados_celsius(grados_farenheit) == expected