#Programa para generar contraseñas aleatorias y de manera segura.
import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '#', '$', '%', '&', '/', '(', ')']
    numeros = ['1','2', '3', '4', '5', '6', '7', '8', '9']
    
    caracteres = mayusculas + minusculas + simbolos + numeros
    
    contrasena = []
    
    for i in range(10):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    #convertir a string de la lista contraseña.
    contrasena = ''.join(contrasena)
    
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()