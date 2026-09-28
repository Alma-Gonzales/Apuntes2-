#Alma Leticia DOuglas Gonzales Guilbert
#Un estudiante desea saber cual su calificacion
#final en el curso de Algoritmo, con los siguientes
#items de califiacion: primer parcial 20% , segundo 
#parcial: 20% Practica: 35 % Parcial final: 25%



print("Primer parcial:")
primer_parcial = float(input())

print("Segundo parcial:")
segundo_parcial = float(input())

print("Practica:")
practica = float(input())

print("Parcial final:")
parcial_final = float(input())

calificacion_final = (primer_parcial * 0.20) + (segundo_parcial * 0.20) + (practica * 0.35) + (parcial_final * 0.25)

print("Calificacion final:", calificacion_final)
