#Apunte 3 Calcular el iva 16% de una venta, subtotal y total.
#Solicitar precio y cantidad del producto
#Alma Leticia Douglas Gonzales Guilbert

precio = float(input("Precio del producto $: "))
cantidad = int(input("Cantidad del Producto: "))

subtotal = precio * cantidad
iva = subtotal * 0.16
total = subtotal + iva

print(f"Subtotal $: {subtotal:.2f}")
print(f"IVA $: {iva:.2f}")
print(f"Total $: {total:.2f}")