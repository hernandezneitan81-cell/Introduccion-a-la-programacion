# 1. imaginate que acabas de abrir una nueva cuenta de ahorro que te ofrece el 4 % de interes del año, estos ahorros debido a los intereses, que ni se cobran hasta finales del año se te añade al valance de tu cuenta de ahporri

# escribir un progama que comiene leyendo la cantidad de   dinero depositada en la cuenta de ahorros, introducida en la ciuenta del usuario
# despues el programa debe de calcular y mostrar por pantallas la cantidad de ahorro tras el primer, segundo y tercer año
#capital * tasa de intere * tiempo del año

#

tiempo_anios = input("ingresa la cantidad de anios: ")
anios = float(tiempo_anios)

tasa_interes = input ("ingresa la tasa de interes anual (%): ")
tasa = float(tasa_interes)

capital_texto = input("ingresa la capital inicial: ")
capital = float(capital_texto)




resultado = capital * tasa * anios


print("cantidad de ahorro en la cuenta de usuario {resultado} ")


