capital_texto = input("ingresa el capital inicial: ")
capital = float(capital_texto)

tasa_texto = input("ingresa la tasa de interés anual (%): ")
tasa = float(tasa_texto)

anios_texto = input ("ingresa la candidad de añios: ")
anios = float(anios_texto)
 
dinero_final = capital * (1+ (tasa / 100)) ** anios

print(f"el dinero que tendras es : ${dinero_final}")