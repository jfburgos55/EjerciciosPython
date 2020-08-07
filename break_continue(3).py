#Utilizando break con while 
def run():
    print("""
        PROGRAMA WHILE CON BREAK
        
        Imprimir datos en pantalla, de acuerdo a la cantidad digitada.
    """)
    
    valor_ingresado = int(input('Ingresa un número: '))
    j = 0
    while  j <= valor_ingresado:
        for i in range(valor_ingresado):
            print(i)
            i += 1
        break

if __name__ == '__main__':
    run()