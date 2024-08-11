# cantidad de payasos y muñecas vendidos
payasos = int(input("Introducir el número de payasos vendidos: "))
muñeca = int(input("Introducir el número de muñecas vendidas: "))

#El peso total de los payasos
p_payasos = payasos * 112

#El peso total de las muñecas
p_muñeca = muñeca * 75

#peso total del paquete
peso_t = p_payasos + p_muñeca

# Se muestra el peso total del paquete
print("El peso total del paquete es de:", peso_t, "gramos")