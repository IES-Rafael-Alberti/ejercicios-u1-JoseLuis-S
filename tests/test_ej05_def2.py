import pytest
from src.ej05_def2 import calcula_precio

@pytest.mark.parametrize(
    "importe, iva, expected",
    [
        (100, 21, 121),
        (150, 21, 181.5),
        (123.1231, 39.21312321, 171.4),
        (11.21, 300, 44.84),
        (1920.1281, 30, 2496.17),
    ]
)
def test_calcula_precio_params(importe, iva, expected):
    assert calcula_precio(importe, iva) == expected