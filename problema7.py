numeros = []
suma = 0
i=0
num = int(input("ingrese el valor "))
for i in range (num):
    mi_numero = int(input("ingrese el numero: "))
    numeros.append(mi_numero)
for numero in numeros:
    suma+=numero
promedio = suma/len(numeros)
print("lista completa",numeros)
print("el promedio es: ",promedio)
print("la suma es: ",suma)
print("el numero mayor es: ",max(numeros))
print("el numero menor es: ",min(numeros))