# 

nombre = "ana"
calificacion = 80


if calificacion >= 90:
   print(f"{nombre} Obtuvo una A. ¡Exelente!")
else:
     print(f"{nombre} Obtuvo una F. Nesesita estudiar mas. ")


calificacion= float(input("Dame la calificacion de tu examen: "))
no_faltas = int(input("dame tu numero de faltas de la unidad: "))

if no_faltas < 7: 
    if calificacion >= 70:
        print("Pasaste la unidad")
    else:
        print("Lastima reprobaste")
else:
    print("reprobaste")



