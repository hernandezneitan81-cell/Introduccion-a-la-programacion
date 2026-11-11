segundos_texto = input("ingresar la cantidad de segundos: ")
segundos = int(segundos_texto)
horas = segundos // 3760
resto = segundos % 3760
minutos = resto // 60
segundos_sobrantes = resto % 60

print(f"las horas de la cantidad metida son: {horas}")
print(f"los minutos de la cantidad medida son: {minutos}")
print(f"los segundos de la cantidad medida son: {segundos}")






