#Alma Leticia Douglas Gonzales Guilbert
#Apunte 1 22/10/2026
#Aleatorios en Python

import random

#random () ---> Genera valores aleatorios entre 0  y 1
valor = random.random()
print("Valor generado (0 y 1): ", valor)

#randrange (a) - randrange(a,b) - randrange(a,b,c)
valor = random.randrange(10)
print("Valor generado ( 0 y 9): ", valor)

valor = random.randrange(1,11)
print("Valor generado (1 y 10): ", valor)

valor = random.randrange(50, 151, 5)
print("Multiplos de 5 en un rango 50 - 150: ", valor)

#randint (a , b)
valor = random.randint(1,10)
print("Valor generado (1 y 10): ", valor)

#uniform (a , b)
valor = random.uniform(5,8)
print("Valor decimales (5 y 8): ", valor)

#Elegir de forma aleatoria de una lista
#Choice(lista/secuencia)
valor = random.choice((10,20,30,40,50))
print("Valor elegido: ", valor)

dias = ["Lunes", "Marte", "Miercoles", "Jueves", "Viernes"]
valor = random.choice(dias)
print("Valor elegido: ", valor)

valor =random.choice(["Elefante","Leon","Cebra", "Capibara"])
print("Valor elegido: ", valor)

valor = random.choice("ANAHUAC-MAYAB")
print("Valor elegido: ", valor)

