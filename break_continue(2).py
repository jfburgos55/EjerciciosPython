#Código para probra el break en python con texto.
def run():
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)
    

if __name__ == '__main__':
    run()