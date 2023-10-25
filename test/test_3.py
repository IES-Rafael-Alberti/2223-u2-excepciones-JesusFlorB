from src.ejercicio3 import (obtener_numero, cuenta_atras)
import pytest

def test_obtener_numero(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: '5\n')
    assert obtener_numero() == 5

    monkeypatch.setattr('builtins.input', lambda _: '-3\n')
    assert obtener_numero() == -3

def test_cuenta_atras():
    assert cuenta_atras(5) == '5, 4, 3, 2, 1, 0'
    assert cuenta_atras(0) == '0'

def test_cuenta_atras_error():
    with pytest.raises(ValueError):
        cuenta_atras(-5)