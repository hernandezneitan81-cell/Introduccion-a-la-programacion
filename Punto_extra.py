costo_entrada = int(input("Dame un numero: "))
entrada_adulto = 90
entrada_nino = 50
entrada_estudiante = 35
entrada_mayor = 30

resultado = costo_entrada

if entrada_adulto >= 18:
    print(f"La entrada costara ${resultado} ")
    if entrada_nino <17: 
        print(f"La entrada costara ${resultado}")
        if entrada_mayor >= 60:
             print(f"La entrada costara ${resultado}")
            
else:
    print(f"La entrada costara ${resultado}")


entrada_estudiante = (input("¿Tiene credencial? "))


