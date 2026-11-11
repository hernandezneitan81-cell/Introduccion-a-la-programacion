#Crea un programa que pida al usuario ingresar una contraseña. Mientras el usuario no escriba exactamente "python123", el programa debe seguir preguntando: "Contraseña incorrecta, intenta de nuevo:
# ". Cuando finalmente escriba la correcta, el programa debe mostrar el mensaje: 
# "¡Acceso concedido!" y terminar.

contrasena = input("Ingresa la contraseña: ")

while contrasena != "python123": 
    contrasena = input("Contraseña incorrecta, intenta de nuevo: ")
print("¡Acceso concedido!")

