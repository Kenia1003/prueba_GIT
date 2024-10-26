import pytest
from PruebaSUMA import suma

def test_suma_numeros():
    assert suma(2, 3) == 5
    assert suma(10, 5) == 15
    assert suma(0, 0) == 0
    assert suma(-2, 2) == 0
    assert suma(3.5, 2.5) == 6

def test_suma_error():
    with pytest.raises(ValueError):
        suma('a', 2)
    with pytest.raises(ValueError):
        suma(2, 'b')
    with pytest.raises(ValueError):
        suma('a', 'b')
