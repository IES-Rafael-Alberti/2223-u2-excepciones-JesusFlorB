from src.ejercicio4 import obtener_numero

def test_obtener_numero_valido(monkeypatch):
    # Simula entrada de usuario válida
    monkeypatch.setattr('builtins.input', lambda _: '5\n')
    assert obtener_numero() == 5

def test_obtener_numero_invalido(monkeypatch, capsys):
    # Simula entrada de usuario inválida
    monkeypatch.setattr('builtins.input', lambda _: 'abc\n')
    assert obtener_numero() is None

    captured = capsys.readouterr()
    assert "La entrada no es correcta. Debes ingresar un numero entero." in captured.out

def test_obtener_numero_negativo(monkeypatch):
    # Simula entrada de usuario negativa
    monkeypatch.setattr('builtins.input', lambda _: '-3\n')
    assert obtener_numero() == -3

def test_obtener_numero_cero(monkeypatch):
    # Simula entrada de usuario cero
    monkeypatch.setattr('builtins.input', lambda _: '0\n')
    assert obtener_numero() == 0

def test_obtener_numero_vacio(monkeypatch, capsys):
    # Simula entrada de usuario vacía
    monkeypatch.setattr('builtins.input', lambda _: '\n')
    assert obtener_numero() is None

    captured = capsys.readouterr()
    assert "La entrada no es correcta. Debes ingresar un numero entero." in captured.out
