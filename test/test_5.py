from src.ejercicio5 import verificar_contraseña
import pytest

def test_contraseña_excepcion():
    with pytest.raises(NameError) as excinfo:
        verificar_contraseña("contraseña_incorrecta")
    
    assert str(excinfo.value) == "Incorrect Password!!"