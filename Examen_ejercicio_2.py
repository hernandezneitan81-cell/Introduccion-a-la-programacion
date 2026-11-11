#crea un programa que calcule el area de un circulo y de un triangulo usando una varible ya definida para pi 

#pedimos el radio del circulo y fijamos un valor para pi
radio_circulo = float(input("Dame el radio de tu circulo: "))
pi = float(3.1415)

#mediante la formula obtendremos el resultado del circulo
resultado = pi * radio_circulo **2

#imprimimos el resultado que nos dara el area de nuestro circulo
print(f"El area del circulo es {resultado}")