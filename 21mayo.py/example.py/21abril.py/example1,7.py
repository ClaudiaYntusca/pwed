#cantidad de dinero depositada
deposito_I = float(input("Introducir la cantidad de dinero depositado: "))
tasa_interes = 0.4
for año in range(1, 4):
  interes_anual = deposito_I * tasa_interes
  deposito_I += interes_anual
  saldo_formateado = f"{deposito_I:.2f}"

  #  mostrar el saldo de la cuenta después de cada año
  print(f"Saldo después del año {año}:", saldo_formateado)