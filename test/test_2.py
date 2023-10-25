from src.ejercicio2 import obtener_numero
import pytest
from unittest.mock import patch

def obtener_numero():
    num = int(input("Ingrese un número positivo: "))
    if num <= 0:
        raise ValueError("Debes ingresar un numero entero positivo.")
    return num

def test_obtener_excepcion(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '-5\n')
        with pytest.raises(ValueError) as excinfo:
            obtener_numero()
        
        assert str(excinfo.value) == "Debes ingresar un numero entero positivo."