Cantidad_texto = input("ingresa la cantidad de dinero a retirar: ")
cantidad = int(Cantidad_texto)

billetes_500 = cantidad // 500
resto = cantidad % 500

billetes_200 = resto // 200
resto = resto % 200

billetes_100 = resto // 100

print(f"billetes de $500: {billetes_500}") 
print(f"billetes de $200: {billetes_200}")
print(f"billetes de %100: {billetes_100}")