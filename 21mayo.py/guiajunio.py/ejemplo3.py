# Manejando una excepción KeyError
mi_Diccionario = {"llave3": "valor3", "llave5": "valor5"}
try:
    valor = mi_Diccionario["llave4"]
except KeyError:
    print("La llave no existe en el Diccionario")