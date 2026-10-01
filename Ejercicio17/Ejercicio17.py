# Apunte 5 
# Alma Leticia Douglas Gonzales Guilbert
# Un vendedor recibe un sueldo basico mas una comision
# del 10 % si su venta es menor que 100,000 pesos o del 15%
# si su venta es mayor o igual a 100,000 pesos. 
# El vendedor desea saber cuanto dinero obtendra
# por concept de comision y su sueldo

print("Ingrese sueldo base: ")
sueldoB = int(input())

print ("Ingrese el valor de la venta: ")
valVenta = int(input())

if valVenta < 100000:
    porCom = 10
else: 
    porCom = 15

valCom = valVenta *  porCom /100
sueldoNet = sueldoB + valCom 

print("Porcentaje de comision: ", porCom)
print("Valor de comision: ", valCom)
print("Sueldo Neto: ", sueldoNet)
