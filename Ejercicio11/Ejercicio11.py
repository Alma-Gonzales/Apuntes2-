#Determinar el porcentaje de hombres y mujeres
#presentes en el curso de algoritmos, si conoce
#el numero de hombres y mujeres que tiene

print("Ingrese el numero de hombres: ")
hombres = int(input())

print("Ingrese el numero de mujeres: ")
mujeres = int(input())

total = hombres + mujeres

porhombres = (hombres / total) * 100
pormujeres = (mujeres / total) * 100

print("Porcentaje de hombres:", porhombres, "%")
print("Porcentaje de mujeres:", pormujeres, "%")
