# Apunte 6 
# Alma Leticia Douglas Gonzales Guilbert
# 

compra= float(input("Ingresa el valor de la compra: "))
if compra >= 500000:
    des = compra * 0.30
elif compra >= 40000:
    des = compra * 0.25
elif compra >= 300000:
    des = compra * 0.20
elif compra >= 200000:
    des = compra * 0.15
elif compra >= 100000:
    des = compra * 0.10
else:
    des = 0 

    total = compra - des
    print("Descuentos: ", des)
    print("Total a Pagar: ", total)