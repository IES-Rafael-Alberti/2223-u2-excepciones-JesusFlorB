"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás 
desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto."""

def obtener_numero():
    try:
        numero = int(input('Por favor, ingresa un numero entero positivo: '))
        if numero <= 0:
            raise ValueError("Debes ingresar un numero entero positivo.")
        return numero
    except ValueError:
        print('Por favor, ingresa un numero entero valido.')
        return obtener_numero()

def cuenta_atras(numero):
    if numero == 0:
        return '0'
    return ', '.join(map(str, range(numero, -1, -1)))


if __name__ == '__main__':
    
    numero = obtener_numero()
    mostrar_cuenta_atras = cuenta_atras(numero)
    print(f'La cuenta atras desde {numero} hasta 0 es: {mostrar_cuenta_atras}')