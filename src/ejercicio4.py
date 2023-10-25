"""Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, 
mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada."""

def obtener_numero():
    try:
        numero = int(input('Por favor, ingresa un numero entero: '))
        return numero
    except ValueError:
        print('La entrada no es correcta. Debes ingresar un numero entero.')
        return obtener_numero()

if __name__ == '__main__':
    
    numero = obtener_numero()
    print(f'El numero ingresado es: {numero}')