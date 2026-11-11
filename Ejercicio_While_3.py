# Haz un programa que le pida al usuario dos cosas:
# una palabra y un número. 
# Luego, usando un bucle while, el programa debe imprimir esa palabra en la pantalla tantas veces como indique el número. 
# Por ejemplo, si el usuario escribe "Hola" y "3", el programa imprimirá "Hola" tres veces.

palabra = input("Inserta tu frase: ")
limite = int(input(" ¿Cuantas veces quieres que se repita?: "))

contador = 1 
while contador <= limite:
    print(palabra)
    contador += 1

