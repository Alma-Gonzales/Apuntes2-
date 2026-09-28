#Alma Leticia DOuglas Gonzales Guilbert
#Un estudiante desea saber cual su calificacion
#final en el curso de Algoritmo, con los siguientes
#items de califiacion: primer parcial 20% , segundo 
#parcial: 20% Practica: 35 % Parcial final: 25%



print("Primer parcial:")
primparcial = float(input())

print("Segundo parcial:")
segparcial = float(input())

print("Practica:")
practica = float(input())

print("Parcial final:")
parcialfin = float(input())

calificacion_final = (primparcial * 0.20) + (segparcial * 0.20) + (practica * 0.35) + (parcialfin * 0.25)

print("Calificacion final:", calificacion_final)
