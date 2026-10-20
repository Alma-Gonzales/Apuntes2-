#Ejercicio1 20/10/2026
#Alma Leticia Douglas Gonzales Guilbert
#Declare una lista de numeros con los siguientes
#valores: 10,21,4,45,66,93,11
#Imprima los elementos de la lista utilizando un ciclo
#Determine cuantos son pares y cuantos son impares


#----------------------------------------------------------------
numeros = [10, 21, 4, 45, 66, 93, 11]

pares = 0
impares = 0

print("Elementos de la lista:")

for numero in numeros:
    print(numero, end=" ")

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print()
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)



