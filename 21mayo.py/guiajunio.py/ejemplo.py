#manejando una execion con ZeroDivisionError
try:
    resultado= 34/0
except ZeroDivisionError:
    print("no se puede dividir un numero entre cero")