#datos del producto
No_producto = input("Introduce el nombre del producto: ")
pre_unitario = float(input("Introduce el precio unitario del producto (con dos decimales): "))
nu_unidades = int(input("Introduce el número de unidades: "))

#precio unitario con 6 dígitos enteros y 2 decimales
precio_unitario_str = f"{pre_unitario:.2f}"
precio_unitario_str = precio_unitario_str.zfill(8)  # Rellenar con ceros a la izquierda hasta tener 8 dígitos

#  unidades con 3 dígitos
numero_unidades_str = f"{nu_unidades:03d}"

# el costo total
coste_t = pre_unitario * nu_unidades

#coste total con 8 dígitos enteros y 2 decimales
coste_t_str = f"{coste_t:.2f}"
coste_t_str = coste_t_str.zfill(10)  # la izquierda hasta tener 10 dígitos

# información del producto
print(f"{No_producto} - Precio: {precio_unitario_str} - Unidades: {numero_unidades_str} - Coste total: {coste_t_str}")