#Ejercicio2 20/10/2026
#Alma Leticia Douglas Gonzales GUilbert
#Pide a un usuario agregar 10 valores a una lista
#(Los valores pueden ser numericos, reales o cadenas)
#Imprime los valores de la lista 
#Luego invierte los elementos de la lista y muestralos
#Ejemplo:[45,21,85,78,99,1,0,78,33,10]
#Salida : [10,33,78,0,1,99,78,85,21,45]

# -----------------------------------------------------------
val = []

for i in range(10):
    valor = input("Ingresa un valor: ")
    val.append(valor)

print("Lista:", val)

val.reverse()
print("Lista invertida:", val)