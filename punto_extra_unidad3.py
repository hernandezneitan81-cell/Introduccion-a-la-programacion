# Crear un programa que simule la validacion de un pin bancario
# El usuario debe adivinar el PIN correcto ( por ejemplo, 1234), pero solo tiene un mkaximo de 3 intentos,
# imprime "acceso concedido" y termina. Si falla, le restas un intento y le dicen cuantas le quedan
# Si se queda sin intentos, imprime "Tarjeta bloqueada" y finaliza

nip = input("Ingrese su contraseñas: ")
limite = 3

while nip != "sixseven" : 
    nip = input("Acceso denegado, intenta de nuevo")

    if "pin usuario" == "nip": 
        print("Acceso concedido")
    else:
        print("Acceso denegado, intentelo de nuevo")