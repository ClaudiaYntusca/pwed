import math
def calculararea(radio,alto):
    areacirculo = math.pi* (radio**2)
    generatiz=14
    volcilindro =2*math.pi * radio * generatiz

    print("El area del circulo es: ",areacirculo)
    print("El volumen del cilindro es: ",volcilindro)

radio=float(input("INGRESA RADIO DEL CIRCULO: "))
alto=float(input("INGRESA LA ALTURA DEL CILINDRO: "))
calculararea(radio,alto)
