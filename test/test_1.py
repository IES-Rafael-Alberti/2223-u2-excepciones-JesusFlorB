from src.ejercicio1 import obtener_edad
import pytest

def test_obtener_edad(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: '30')
    assert obtener_edad() == 30
    

    monkeypatch.setattr('builtins.input', lambda _: '-10')
    with pytest.raises(ValueError) as excinfo:
        obtener_edad()
    assert str(excinfo.value) == "La edad no puede ser negativa."
    

    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    with pytest.raises(ValueError) as excinfo:
        obtener_edad()
    assert str(excinfo.value) == "Por favor, ingresa un numero entero."