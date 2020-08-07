#Estructuras de datos.
#Diccionarios # Funcionan con llaves y valores.
def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }   
    #print(mi_diccionario['llave1'])
    #print(mi_diccionario['llave2'])
    #print(mi_diccionario['llave3'])
    
    poblacion_paises = {
        'Argentina': 44560,
        'Brasil': 209469,
        'Colombia': 50000,
    }
    
    #print(poblacion_paises['Argentina'])
    #Imprime las llaves.
    #for pais in poblacion_paises.keys():
    #   print(pais)
    
    #Imprimir los valores
    #for pais in poblacion_paises.values():
    #    print(pais)
    
    #Imprimir los dos valores
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes.')

if __name__ == '__main__':
    run()