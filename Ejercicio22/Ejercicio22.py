#Alma Leticia Douglas Gonzales Guilbert
#Un almacen de pedidos por correo vende cinco productos,
#los precios son los siguientes:
#-producto1: $2.98 
#-producto2: $4.50
#-producto3: $9.98
#-producto4: $4.49
#-producto5: $6.87

#Escriba un programa que solicite el numero del producto y la cantidad vendida.
#El programa debe determinar el precio de venta de cada producto, calcular y 
#mostrar el valor total del producto.


numPro = int(input("Ingrese el numero del producto 1 al 5: "))
canVen = int(input("Ingrese la cantidad vendida: "))

if numPro == 1:
    preVen = 2.98
elif numPro == 2:
    preVen = 4.50
elif numPro == 3:
    preVen = 9.98
elif numPro == 4:
    preVen = 4.49
elif numPro == 5:
    preVen = 6.87
else:
    preVen = 0
    print("Error: El producto no existe")

print(f"El precio de venta del producto {numPro}: ${preVen:.2f}")

valTot = canVen * preVen

print(f"Total de la venta: ${valTot:.2f}")