"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas."""

def obtener_numero():
    try:
        numero = int(input('Por favor, ingresa un numero entero positivo: '))
        if numero <= 0:
            raise ValueError("Debes ingresar un numero entero positivo.")
        return numero
    except ValueError:
        print('Por favor, ingresa un numero entero valido.')
        return obtener_numero()  # Llamada recursiva

def numeros_impares_hasta(numero):
    impares = [str(i) for i in range(1, numero+1, 2)]
    return ', '.join(impares)

if __name__ == '__main__':
    
    numero = obtener_numero()
    impares = numeros_impares_hasta(numero)
    print(f'Los numeros impares hasta {numero} son: {impares}')