# # Alma Leticia Doouglas Gonzales Guilbert
# Apunte 2 
# Realiza un algoritmo que lea o capture dos valores 
# Si el primer valor es menor al segundo valor, hacer 
# la suma; de lo contrario hacer la diferencia (resta)
# Si son iguales hacer la multiplicacion. 

print("Valor No1.: ")
valor1 = int(input())

print("Valor No2.: ")
valor2 = int(input())

#Proceso parciales
if valor1 < valor2: 
    res = valor1 + valor2
else: 
    if valor1 > valor2:
        res = valor1 - valor2
    else:
        res = valor1 * valor2
print ("Resultado: ", res)
