#Apunte 1 20/10/2026
#Alma Leticia Douglas Gonzales Guilbert
#               Diferencias
# C++ (Arreglos)       |  Python (Listas)  
# Size es fijo         |  Size dinamico   
# Son de un mismo tipo |  Pueden ser del mismo tipo o combinados
# 
# Similares
# - Acceso a los elementos
# - Posicion (indice)
# Para curiosos --> arrays con numpy


#Declarar o definir listas en Python  

#Listas vacias
lista =[]
print(lista)

#Listas con elementos numericos
primos = [2,3,6,7,11,13]

#Lista con elementos cadenas
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(primos)
print(dias)

#Lista con elementos combinados
fecha = [20, "Octubre",2026, 8.49]
print(fecha)

#Lista de listas
peliculas = [["Spider-man Brand new day", 2026] ,["El retorno del rey", 2023]]
print(peliculas)

lista = [primos, dias,fecha]
print(lista)