#Alma Leticia Douglas Gonzales Guilbert
#En python la estructura SEGUN (SWITCH)
#---------NO EXISTE--------------------
#Se emula con los if - else

print("Ingresa un numero del 1 al 7: ")
dia = int(input())

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Error: El numero debe de estar entre 1 y 7.")
