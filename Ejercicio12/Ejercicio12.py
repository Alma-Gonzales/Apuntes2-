#Calcular el area y perimitro de un triangulo
#asumir que es un triangulo equilatero


print("Ingrese la base del triangulo: ")
base = float(input())

print("Ingrese la altura del triangulo: ")
altura = float(input())

area = (base * altura) / 2
perimetro = base * 3

print("Area del triangulo:", area)
print("Perimetro del triangulo:", perimetro)
