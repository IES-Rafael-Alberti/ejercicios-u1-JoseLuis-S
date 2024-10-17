import pytest
from src.ej01_def2 import saludo

@pytest.mark.parametrize(
    'nom, expected',
    [
        ('Juan', 'Hola, Juan.'),
        ('pedro', 'Hola, Pedro.'),
        ('MANOLITO', 'Hola, Manolito.'),
        ('rAmIRo', 'Hola, Ramiro.'),
        ('joSEmi', 'Hola, Josemi.'),
    ]
)

def test_saludo_params(nom, expected):
    assert saludo(nom) == expected