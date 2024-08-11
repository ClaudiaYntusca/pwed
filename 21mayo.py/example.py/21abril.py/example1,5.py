#peso y estatura de los usuarios 
estatura=float(input("Introduce tu estatura (en centimetros): "))
peso=float(input("Introduce tu peso (en kg): "))
imc = peso / ( estatura * estatura )
imc_str = f"{imc:.2f}"
#resultado
print("El índice de masa corporal es", imc_str)