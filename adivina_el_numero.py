#Programa para adivinar el número.
import random

def run():
    numero_aleatorio = random.randint(1, 100)
    print("""
        Adivina el número
        
        Rango del 1 al 100 
    """)
    numero_digitado = int(input('Digita un número del 1 al 100: '))
    
    while numero_digitado != numero_aleatorio:
        if numero_digitado < numero_aleatorio:
            print('El número es más GRANDE!!')
        else:
            print('El número es más PEQUEÑO!!')
        numero_digitado = int(input('Digita otro número: '))
    print(' ¡¡GANASTE!! ')
   

if __name__ == '__main__':
    run()