"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
(desde 1 hasta su edad)."""

def mostrar_años(edad):
    for i in range(1, edad + 1):
        print(f'Has cumplido {i} años')

def obtener_edad(entrada=input):
    try:
        edad = int(entrada('Por favor, ingresa tu edad: '))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        return edad
    except ValueError:
        print('Por favor, ingresa un numero entero.')
        return obtener_edad(entrada)


if __name__ == '__main__':
    edad = obtener_edad()
    mostrar_años(edad)