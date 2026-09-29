# Alma Leticia Doouglas Gonzales Guilbert
# Apunte 3

salBas = float(input("Salario basico: "))
tiemSer = int(input("Tiempo de servicio en anios: "))

#Procesos Parciales 

if tiemSer < 5:
    porBon = 5
else:
    if tiemSer < 10: 
     porBon = 10
    else: 
        if tiemSer < 15:
            porBon = 15
        else:
            if tiemSer < 20:
                porBon = 20
            else:
                if tiemSer < 30:
                    porBon = 30
                else:
                    porBon = 50
valBon = salBas * porBon / 100

#Datos de Salida Parciales

print("Porcentaje de bonificacion", porBon)
print("Valor de la bonifiacion: ", valBon)