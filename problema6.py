numero = []
cont=0
while  cont < 5:
    number = int(input("ingrese el numero: "))
    numero.append(number)
    cont+=1
invertidos = numero[::-1]
print("lista completa",numero)
print("lista invertida ",invertidos)
