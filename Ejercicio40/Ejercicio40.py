#Apunte 2 20/10/2026
#Alma Leticia Douglas Gonzales Guilbert

primos = [2,3,6,7,11,13]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
lista = [primos, dias]
peliculas = [["Spider-man Brand new day", 2026] ,["El retorno del rey", 2023]]


#Imprimir el valor 11 de la lista primos
print(primos[4])

#Imprimir Lunes de la lista dias
print(dias[0])

#Imprimir el 3er elemento de la lista en la posicion 1 de lista []
print(lista[1][2])

#Imprimir el titulo de la primera pelicula
print(peliculas[0][0])

#Acceder a todos los elementos de la lista primos con un ciclo
print()
for i in range(6):
    print(primos[i], end =" ")

#Acceder a todos los elementos de la lista dias con un ciclo
print()
for i in dias:
    print(i, end=" ")

print()