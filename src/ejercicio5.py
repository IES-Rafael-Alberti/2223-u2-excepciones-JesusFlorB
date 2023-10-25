"""Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, 
"Incorrect Password!!"""

def verificar_contraseña(contraseña):
    contraseña_correcta = "contraseña"

    if contraseña != contraseña_correcta:
        raise NameError("Incorrect Password!!")

if __name__ == '__main__':
    
    try:
        contraseña_usuario = input('Ingresa la contraseña: ')
        verificar_contraseña(contraseña_usuario)
        print('Contraseña correcta. Acceso concedido.')
    except NameError as i:
        print(i)