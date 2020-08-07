def conversor(tipo_pesos, valor_dolar):
    #Solicitar el valor de los pesos.
	pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
	pesos = float(pesos)
	#Convertir valores
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2)
	dolares = str(dolares)
	#Mostrar en pantalla
	print("Tienes $" + dolares + " dolares.")

menu = """
BIENVENIDO AL CONVERSOR DE MONEDAS 💰

1-PESOS COLOMBIANOS
2-PESOS ARGENTINOS
3-PESOS MEXICANOS

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
	conversor("argentinos", 65)    
elif opcion == 3:
	conversor("mexicanos", 24)    
else:
	print("Ingresa una opción correcta!! 🤦‍")