# Escribe un programa que utilice un bucle while para imprimir la tabla de multiplicar del número 5. 
# El programa debe mostrar los resultados desde el 5 x 1 = 5 hasta el 5 x 10 = 50.

multiplicacion = 1

while multiplicacion <= 10:
    resultado = 5 * multiplicacion
    print(f" 5 X {multiplicacion} = {resultado}")
    multiplicacion += 1

