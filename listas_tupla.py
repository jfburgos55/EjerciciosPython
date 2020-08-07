#Definición de listas.

#Creando la lista -> Listas son objetos dinamicos.
numeros = [1, 2, 3, 4, 5]
#Agregando numero a la lista
numeros.append(6)
#Imprimir el valor de la lista.
print(numeros)


#Creando lista dos
numeros2 = [7, 8, 9]

#Concatenar las listas
lista_final = numeros + numeros2

print(lista_final)

#Creacion de tupla -> Tuplas son objetos estaticos.
mi_tupla = (1, 2, 3, 4, 5)

print(mi_tupla)

for numero in mi_tupla:
    print(numero)
