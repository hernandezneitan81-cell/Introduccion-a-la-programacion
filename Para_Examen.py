calificacion = [45, 91, 78, 60, 33, 85, 100, 52]
nume = 0

while nume <=len(calificacion) -1:
    if calificacion[nume] < 50:
        print(f"Reprobado{calificacion[nume]}")
        if calificacion[nume] > 50:
            print(f"Recuperacio{calificacion[nume]}")
            if calificacion[nume] >70:
                print(f"Aprobado{calificacion[nume]}")
    else:
        calificacion[nume] >= 90
        print(f"Sobresaliente{calificacion[nume]}")
        nume = nume +1
