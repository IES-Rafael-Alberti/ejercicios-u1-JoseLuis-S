import pytest
from src.ej02_def2 import pagoTotal

@pytest.mark.parametrize(
    'horas, precioHoras, expected',
    [
        (10, 8, 80),
        (20.2312, 21.3213, 431.36),
        (100000000, 1, 100000000),
        (25.2, 34, 856.8),
        (-123, 9.4, -1156.2),
    ]
)
def test_pagoTotal(horas, precioHoras, expected):
    assert pagoTotal(horas, precioHoras) == expected