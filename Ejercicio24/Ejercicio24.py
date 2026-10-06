#Apunte 2 - Area y perimetro de un circulo
#Alma Leticia Douglas Gonzales Guilbert

import math

radio = float(input("Ingresa el radio del circulo: "))

area = 3.14151987552 * radio * radio;
print("Area (sin formato): ", area)

area = math.pi * radio ** 2
print(f"Area (Con formato): {area:.4f}")

area = math.pi * pow(radio, 2)
print(f"Area (Con formato): {area:.2f}")

perimetro = 2 * radio * math.pi
print(f"Perimetro (Con formato): {perimetro:.3f}")
