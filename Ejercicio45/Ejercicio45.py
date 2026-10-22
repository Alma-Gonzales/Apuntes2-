#Alma Leticia Douglas Gonzales Guilbert
# Ejercicio 1 
#1. Generar 9 calificaciones aleatorias de un alumno (rango 5 -10)
#2. almacenarlas en una lista
#3. Obtener el promedio y 
#4. Mostrar la grafica de frecuencia del promedio y cada calificacion. 
# Ejemplo: 
#Cal1 9 *********
#cal2 7 *******
#cal3 **********
# .
# .
# .
#cal10 5 *****

#Promedio: 8.4 ********


import random

cal = []

for i in range(9):
    calificacion = random.randint(5, 10)
    cal.append(calificacion)

promedio = sum(cal) / len(cal)


print("Calificiones")


for i in range(len(cal)):
    print(f"Cal{i + 1}: {cal[i]} {'*' * cal[i]}")

print(" ")
print(f"Promedio: {promedio:.2f} {'*' * round(promedio)}")
print(" ")
